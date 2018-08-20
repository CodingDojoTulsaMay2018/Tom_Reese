import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  questionarr = [
    ["what is your favorite color?","blue"],
    ["what is your quest?","a minivan"],
    ["what is Kramer's first name?","Cosmo"],
    ["who is the best monopoly deal player?","Tom"],
    ["the answer to the most important question","42"]
  ]
  shinto_val = 1
  mined = 0
  history = []
  transaction: object
 
  constructor(private _http: HttpClient) {

   }

   addVal(num, action){
    console.log(this.shinto_val," is our current coin value"); 
    while(num > 0){
      var random = this.onRandom()
      this.shinto_val++
      this.mined++
      this.history.push([this.shinto_val, action, random])
      num--
    }
    console.log(this.history);
    return this.shinto_val
   }

   onRandom(){
     return Math.floor((Math.random() * 9999) + 1)
   }

   minusVal(num, action){
    console.log(this.shinto_val," is our current coin value"); 
    while(num > 0){
      var random = this.onRandom()
      this.shinto_val--
      this.mined--
      this.history.push([this.shinto_val, action, random])
      num--
    }
    console.log(this.history);
      return this.shinto_val
    }

}