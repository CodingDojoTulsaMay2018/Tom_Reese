import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpService } from '../http.service';
import { Raptor } from '../raptor';


@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.css']
})
export class EditComponent implements OnInit {

  editRaptor: Raptor
  error = ""

  constructor(
    private httpService: HttpService,
    private _route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit() {
    this._route.params.subscribe(params => {
      console.log(params['id']);
      this.httpService.getRaptor(params['id']).subscribe(auth => {
        this.editRaptor = auth as Raptor
        console.log('raptor', this.editRaptor);
      });
    });
  }


onUpdate() {
  this.httpService.putRaptor(this.editRaptor['_id'],this.editRaptor).subscribe(data =>{
    console.log(data["message"])
    if(data['errors']){
      this.error = data['message']
    }  
    else{
      this._router.navigate(['/']);

    }
})}

onDelete(id){
  console.log("deleting ",id);
  let observable = this.httpService.deleteRaptor(id);
  observable.subscribe()
  this._router.navigate(['/']);

  }

  goHome(){
    this._router.navigate(['/']);
  }

}
