import { HttpService } from './http.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  greet = 'My Tasks';
  tasks: any;
  showing: any;
  newTask: any;
  update: any;

  onButtonClickParam(str: String): void { 
    // console.log(str);
    // console.log(`Click event is working with animal id: ${str["i"]}`)
    // this.showAnimalsFromService(str["i"])
    ;}

  constructor(private _httpService: HttpService){}
  // ngOnInit will run when the component is initialized, after the constructor method.
  ngOnInit(){
    this.getTasksFromService();
    this.newTask = { title: "", description: ""}
  }

  showTask(obj: object): void { 
    // console.log(str);
    console.log(`Click event is working with task id: ${obj}`)
    this.showing =obj
    this.update = ""
    ;}

    updateTask(obj: Object): void{
      this.update = obj;
      this.showing = ""
    }

  onshowAll() {
    console.log("showing all");
    
   this.getTasksFromService()
  }

  onSubmit() {
   this.postTasksFromService(this.newTask) 
   this.newTask = { title: "", description: ""}
  }

  onUpdate() {
    this.updateTaskFromService(this.update) 
   }

  onClear() {
     this.showing= ""
   }


  onDelete(id){
    console.log(id, "grabbed the id from HTML");
    
    this.deleteTaskFromService(id);
    this.showing= ""
  }

  getTasksFromService(){
    let observable = this._httpService.getTasks();
    observable.subscribe(data => {
       console.log("Got our tasks!", data)
       this.tasks = data;
       console.log(this.tasks)
    });
  }

  getTaskFromService(id){
    let observable = this._httpService.getTask(id);
    observable.subscribe(data => {
      //  console.log("Got our tasks!", data)
       this.showing = data;
       console.log(this.showing," this is the task we are showing")
    });
  }

  postTasksFromService(data){
    let observable = this._httpService.postTasks(data);
    observable.subscribe(data => {
      //  console.log("Got our tasks!", data)
       this.tasks = data;
      //  console.log(this.tasks)
      this.getTasksFromService()
    });
  }

  deleteTaskFromService(id){
    console.log(id," is the id");
    
    let observable = this._httpService.deleteTask(id);
    observable.subscribe(data =>{
      this.showing =""
      this.getTasksFromService()})
  }

  updateTaskFromService(data){
    let id = data._id
    let observable = this._httpService.putTasks(id,data);
    observable.subscribe(data =>{
      this.update = ""
      this.getTasksFromService()})
      this.showing =data
  }
}


