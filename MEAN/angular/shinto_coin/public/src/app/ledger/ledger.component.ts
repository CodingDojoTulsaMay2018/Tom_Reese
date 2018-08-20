import { Component, OnInit } from '@angular/core';
import { HttpService } from './../http.service';

@Component({
  selector: 'app-ledger',
  templateUrl: './ledger.component.html',
  styleUrls: ['./ledger.component.css']
})
export class LedgerComponent implements OnInit {
  history = this._httpService.history

  constructor(private _httpService: HttpService) { }

  ngOnInit() {
  }

  grabId(obj){
    this._httpService.transaction = obj;
    console.log(obj);
    
  }

}
