import { Frisbee } from './frisbee';
import { HttpService } from './http.service';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  greet = 'My Frisbees';
  frisbees: any;
  showing: any;
  newFrisbee = new Frisbee();
  update: any;
  ratedFrisbee: any

  constructor(private _httpService: HttpService){}
  ngOnInit(){
    this.getFrisbeesFromService();
    this.newFrisbee = { title: "", description: ""}
  }

  showFrisbee(obj: object): void { 
    console.log(`Click event is working with frisbee id: ${obj}`)
    this.showing =obj
    this.update = ""
    ;}

    updateFrisbee(obj: Object): void{
      this.update = obj;
      this.showing = ""
    }

  onshowAll() {
    console.log("showing all");
   this.getFrisbeesFromService()
  }

  onSubmit() {
   this._httpService.postFrisbees(this.newFrisbee).subscribe(data => {
      this.frisbees = data;
   });
   this.newFrisbee = { title: "", description: ""}
  }

  onUpdate() {
    this._httpService.putFrisbees(this.update.id,this.update).subscribe(data =>{
      this.update = ""
      this.showing =data})
      this.getFrisbeesFromService()
   }

  onClear() {
     this.showing= ""
   }

  onDelete(id){
    this._httpService.getFrisbee(id).subscribe(data => {
      this.showing = data;
      console.log(this.showing," this is the frisbee we are showing")
    });
    this._httpService.getFrisbees()
  }

  getFrisbeesFromService(){
    let observable = this._httpService.getFrisbees();
    observable.subscribe(data => {
       console.log("Got our frisbees!", data)
       this.frisbees = data;
       console.log(this.frisbees)
    });
  }

  rateFrisbee(id){
    // console.log("Called rateCake ");
    // console.log(this.ratedCake);
    // console.log("Stars :" +this.ratedCake.stars);
    // console.log("Id :" +id)
    // console.log("Stars :" +this.ratedCake.comment);
    

    this.ratedFrisbee = {stars:this.ratedFrisbee.stars,
                 comment: this.ratedFrisbee.comment}
    this._httpService.rateFrisbees(this.ratedFrisbee).subscribe(data=>{this,this.ratedFrisbee = data;})
}
}