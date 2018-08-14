import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private _http: HttpClient) {
    this.getTasks();
   }

   getTasks(){
     return this._http.get('/tasks');
   }

   postTasks(task){
    return this._http.post('/tasks', task);
  }

  getTask(id){
    return this._http.get('/tasks/'+id);
  }

  putTasks(id,task){
    return this._http.put('/tasks/'+id, task);
  }

  deleteTask(id){
    return this._http.delete('/tasks/'+id);
  }
}