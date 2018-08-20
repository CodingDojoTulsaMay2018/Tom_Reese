import { Component, OnInit } from '@angular/core';
import { HttpService } from './../http.service';

@Component({
  selector: 'app-mine',
  templateUrl: './mine.component.html',
  styleUrls: ['./mine.component.css']
})
export class MineComponent implements OnInit {
  question = this._httpService.questionarr
  attempt = ''
  reply =''
  constructor(private _httpService: HttpService) { }

  ngOnInit() {
  }

  onAnswer(event){
    event.preventDefault() 
    if(this.attempt == this.question[this.question.length-1][1]){
      console.log("got it");
      this.reply = "CORRECT!"
      this.question.pop()
      this.attempt=''
      this._httpService.addVal(1, "Mined")
    }
    else{
      console.log("missed it");
      this.reply = "WRONG!" 
      this.attempt=''
    }
  }

}
