import { HttpService } from './http.service';
import { Component, OnInit } from '@angular/core';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Restful Tasks API';
  tasks: any
  showing: any
  showAll: any


  showTask(obj: object): void { 
    // console.log(str);
    console.log(`Click event is working with task id: ${obj}`)
    this.showing =obj
    ;}
 
  constructor(private _httpService: HttpService){}
  // ngOnInit will run when the component is initialized, after the constructor method.
  ngOnInit() {

  }
  
  onshowAll() {
     console.log("showing all");
     
    this.getTasksFromService()
   }

  getTasksFromService(){
    let observable = this._httpService.getTasks();
    observable.subscribe(data => {
       this.tasks = data;
       console.log(data);       
       console.log(this.tasks," = our tasks");
       this.showAll = true
       
    });
  }

}
