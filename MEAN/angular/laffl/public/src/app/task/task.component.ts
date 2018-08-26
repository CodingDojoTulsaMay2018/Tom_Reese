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
  players

  constructor(
    private httpService: HttpService,
    private _route: ActivatedRoute,
    private _router: Router,
    private orderPipe: OrderPipe
  ) { }

  ngOnInit() {
    this.players = this.httpService.getPosition('QB').then(data => {
      console.log(data)
    })
  }

}
