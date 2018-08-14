import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { HttpService } from '../http.service';


@Component({
  selector: 'app-frisbee',
  templateUrl: './frisbee.component.html',
  styleUrls: ['./frisbee.component.css']
})
export class FrisbeeComponent implements OnInit {
  // @Input() tom: any
  // @Output() myEvent = new EventEmitter()

  constructor(private _httpService: HttpService) { }

  ngOnInit() {
  }

}
