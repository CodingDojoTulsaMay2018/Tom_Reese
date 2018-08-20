import { Component, OnInit } from '@angular/core';
import { HttpService } from './../http.service';

@Component({
  selector: 'app-buy',
  templateUrl: './buy.component.html',
  styleUrls: ['./buy.component.css']
})
export class BuyComponent implements OnInit {
  coins = this._httpService.mined;
  cost = this._httpService.shinto_val
  number: number
  msg: string

  constructor(private _httpService: HttpService) { }

  ngOnInit() {
    console.log(this.coins);
    
  }

  onBuy(){
    console.log(this.number," is the number we purchased");
    
    this._httpService.addVal(this.number, "Bought")
    this.coins = this._httpService.mined;
    this.cost = this._httpService.shinto_val
    this.msg = "Bought "+this.number+" coins"

  }

}
