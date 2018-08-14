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
  newFrisbee: any;
  update: any;

  onButtonClickParam(str: String): void { 
    // console.log(str);
    // console.log(`Click event is working with animal id: ${str["i"]}`)
    // this.showAnimalsFromService(str["i"])
    ;}

  constructor(private _httpService: HttpService){}
  // ngOnInit will run when the component is initialized, after the constructor method.
  ngOnInit(){
    this.getFrisbeesFromService();
    this.newFrisbee = { title: "", description: ""}
  }

  showFrisbee(obj: object): void { 
    // console.log(str);
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
   this.postFrisbeesFromService(this.newFrisbee) 
   this.newFrisbee = { title: "", description: ""}
  }

  onUpdate() {
    this.updateFrisbeeFromService(this.update) 
   }

  onClear() {
     this.showing= ""
   }


  onDelete(id){
    console.log(id, "grabbed the id from HTML");
    
    this.deleteFrisbeeFromService(id);
    this.showing= ""
  }

  getFrisbeesFromService(){
    let observable = this._httpService.getFrisbees();
    observable.subscribe(data => {
       console.log("Got our frisbees!", data)
       this.frisbees = data;
       console.log(this.frisbees)
    });
  }

  getFrisbeeFromService(id){
    let observable = this._httpService.getFrisbee(id);
    observable.subscribe(data => {
      //  console.log("Got our frisbees!", data)
       this.showing = data;
       console.log(this.showing," this is the frisbee we are showing")
    });
  }

  postFrisbeesFromService(data){
    let observable = this._httpService.postFrisbees(data);
    observable.subscribe(data => {
      //  console.log("Got our frisbees!", data)
       this.frisbees = data;
      //  console.log(this.frisbees)
      this.getFrisbeesFromService()
    });
  }

  deleteFrisbeeFromService(id){
    console.log(id," is the id");
    
    let observable = this._httpService.deleteFrisbee(id);
    observable.subscribe(data =>{
      this.showing =""
      this.getFrisbeesFromService()})
  }

  updateFrisbeeFromService(data){
    let id = data._id
    let observable = this._httpService.putFrisbees(id,data);
    observable.subscribe(data =>{
      this.update = ""
      this.getFrisbeesFromService()})
      this.showing =data
  }
}