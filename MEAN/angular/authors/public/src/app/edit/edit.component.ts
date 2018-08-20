import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '../../../node_modules/@angular/router';
import { HttpService } from './../http.service';
import { Author } from './../author';


@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})
export class EditComponent implements OnInit {

  editAuthor: Author
  error = ""

  constructor(
    private httpService: HttpService,
    private _route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit() {
    this._route.params.subscribe(params => {
      console.log(params['id']);
      this.httpService.getAuthor(params['id']).subscribe(auth => {
        this.editAuthor = auth as Author
        console.log('author', this.editAuthor);
      });
    });
  }

  onUpdate() {
    console.log(this.editAuthor," is our update..."+this.editAuthor['_id'])
    let observable = this.httpService.putAuthor(this.editAuthor['_id'],this.editAuthor)
    observable.subscribe(data =>{
      if(data['errors']){
        this.error = data['errors'].name['message']
        console.log(data['errors'])
      }
      else{
        this.editAuthor = data as Author
        this._router.navigate(['/']);
      }
   }
  )}

  goHome(){
    this._router.navigate(['/']);
  }

}
