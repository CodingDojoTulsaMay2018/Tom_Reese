import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '../../../node_modules/@angular/router';
import { HttpService } from './../http.service';
import { Raptor } from './../raptor';

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.css']
})
export class NewComponent implements OnInit {

  newRaptor: Raptor = new Raptor()
  error = ""

  constructor(
    private httpService: HttpService,
    private _route: ActivatedRoute,
    private _router: Router
  ) { }

  ngOnInit() {    
  }

  onAdd() {
    console.log(this.newRaptor," is our new author..."+this.newRaptor)
    this.httpService.postRaptor(this.newRaptor).subscribe(data =>{ 
      if(data['errors']){
        this.error = data['message']
      }  
      else{
        this.newRaptor = data as Raptor
        this._router.navigate(['/']);
      }

   }
  )}

  goHome(){
    this._router.navigate(['/']);
  }

}
