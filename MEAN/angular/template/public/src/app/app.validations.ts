// import { HttpService } from './http.service';
// import { Component, OnInit } from '@angular/core';



// @Component({
//   selector: 'app-root',
//   templateUrl: './app.component.html',
//   styleUrls: ['./app.component.css']
// })
// export class AppComponent implements OnInit {
//   title = 'Endangered Species';
//   animals: any;
//   showing: any;
//   newAnimal: any;

//   onButtonClickParam(str: String): void { 
//     // console.log(str);
//     console.log(`Click event is working with animal id: ${str["i"]}`)
//     this.showAnimalsFromService(str["i"])
//     ;}

//   constructor(private _httpService: HttpService){}
//   // ngOnInit will run when the component is initialized, after the constructor method.
//   ngOnInit(){
//     this.getAnimalsFromService();
//     this.newAnimal = { name: "", population: ""}
//   }

//   onSubmit() {
//    this.postAnimalsFromService(this.newAnimal) 
//     this.newAnimal= { name: "", population: ""}
//   }

//   onClear() {
//      this.showing= ""
//    }


//   getAnimalsFromService(){
//     let observable = this._httpService.getAnimals();
//     observable.subscribe(data => {
//       //  console.log("Got our tasks!", data)
//        this.animals = data;
//       //  console.log(this.tasks)
      
//     });
//   }
//   showAnimalsFromService(id){
//     let observable = this._httpService.showAnimals(id);
//     observable.subscribe(data => {
//       //  console.log("Got our tasks!", data)
//        this.showing = data;
//        console.log(this.showing," this is the animal we are showing")
//     });
//   }

//   postAnimalsFromService(data){
//     let observable = this._httpService.postAnimals(data);
//     observable.subscribe(anim => {
//       //  console.log("Got our tasks!", data)
//        this.animals = data;
//       //  console.log(this.tasks)
//       this.getAnimalsFromService()
//     });
//   }
// }