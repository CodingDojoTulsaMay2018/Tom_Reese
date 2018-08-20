import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '../../../node_modules/@angular/router';
import { HttpService } from './../http.service';
import { Author } from './../author';

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.css']
})
export class NewComponent implements OnInit {

  newAuthor: Author = new Author()
  error = ""

  constructor(
    private httpService: HttpService,
    private _route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit() {
  }

  onAdd() {
    console.log(this.newAuthor," is our new author..."+this.newAuthor)
    this.httpService.postAuthor(this.newAuthor).subscribe(data =>{ 
      if(data['errors']){
        this.error = data['errors'].name['message']
        console.log(data['errors'])
      }
      else{
        this.newAuthor = data as Author
        this._router.navigate(['/']);
      }

   }
  )}

  goHome(){
    this._router.navigate(['/']);
  }

}
