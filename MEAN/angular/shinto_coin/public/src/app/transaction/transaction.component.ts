import { Component, OnInit } from '@angular/core';
import { HttpService } from './../http.service';

@Component({
  selector: 'app-transaction',
  templateUrl: './transaction.component.html',
  styleUrls: ['./transaction.component.css']
})
export class TransactionComponent implements OnInit {
transaction = this._httpService.transaction
  constructor(private _httpService: HttpService) { }

  ngOnInit() {
  }

}
