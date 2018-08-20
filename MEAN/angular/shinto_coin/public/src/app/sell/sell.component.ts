import { Component, OnInit } from '@angular/core';
import { HttpService } from './../http.service';

@Component({
  selector: 'app-sell',
  templateUrl: './sell.component.html',
  styleUrls: ['./sell.component.css']
})
export class SellComponent implements OnInit {
  coins = this._httpService.mined;
  cost = this._httpService.shinto_val
  number: number
  error: string

  constructor(private _httpService: HttpService) { }

  ngOnInit() {
    console.log(this.coins);
    
  }

  onSell(){

    if(this.coins - this.number >= 0){
    console.log(this.number," is the number we sold");    
    this._httpService.minusVal(this.number, "Sold")
    this.coins = this._httpService.mined;
    this.cost = this._httpService.shinto_val
    this.error = "Sold "+this.number+" coins"
    return this.error
  }
  this.error = "You can't sell that many coins!!!"
  return this.error
  
}

}
