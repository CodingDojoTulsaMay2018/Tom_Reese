import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private _http: HttpClient) {
    this.getTasks();
    this.postTasks({
      "title": "potatoe",
      "description" : "brown"
    }),
    this.getTask("5b6c6fada06be034404267e0"),
    this.putTasks("5b6c6fada06be034404267e0",{
      "title": "burrito",
      "description" : "white"
    }),
    this.deleteTask("5b6c6fada06be034404267e0");
   }

   getTasks(){
     let tempObservable = this._http.get('/tasks');
     tempObservable.subscribe(data => console.log("Got our tasks!", data));
   }

   postTasks(task){
    let tempObservable = this._http.post('/tasks', task);
    tempObservable.subscribe(data => console.log("Post our tasks!", data));
  }

  getTask(id){
    let tempObservable = this._http.get('/tasks/'+id);
    tempObservable.subscribe(data => console.log("Got our single task!", data));
  }

  putTasks(id,task){
    let tempObservable = this._http.put('/tasks/'+id, task);
    tempObservable.subscribe(data => console.log("Updated our task!", data));
  }

  deleteTask(id){
    let tempObservable = this._http.delete('/tasks/'+id);
    tempObservable.subscribe(data => console.log("Delete this task!", data));
  }
}
