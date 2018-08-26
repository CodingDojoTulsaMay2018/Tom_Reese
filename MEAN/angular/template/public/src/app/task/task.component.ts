import { Component, OnInit } from '@angular/core';
import { Task } from './../task';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpService } from './../http.service';
import { OrderPipe } from 'ngx-order-pipe';

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {
  editTask: Task
  error = ""

  constructor(
    private httpService: HttpService,
    private _route: ActivatedRoute,
    private _router: Router,
    private orderPipe: OrderPipe
  ) { }

  ngOnInit() {
    this._route.params.subscribe(params => {
      console.log(params['id']);
      this.httpService.getTask(params['id']).subscribe(task => {
        this.editTask = task as Task
        console.log('product: ', this.editTask);
      });
    });
  }

  onUpdate() {
    this.httpService.putTask(this.editTask['_id'],this.editTask).subscribe(data =>{
      console.log(data["message"])
      if(data['errors']){
        this.error = data['message']
      }  
      else{
        this._router.navigate(['/tasks']);
  
      }
  })}
  
  onDelete(id){
    console.log("deleting ",id);
    let observable = this.httpService.deleteTask(id);
    observable.subscribe()
    this._router.navigate(['/tasks']);
  
    }
  
    goHome(){
      this._router.navigate(['/']);
    }


}
