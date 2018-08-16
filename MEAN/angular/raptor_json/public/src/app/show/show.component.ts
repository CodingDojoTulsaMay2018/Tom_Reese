import { Component, OnInit } from '@angular/core';
import { HttpService } from '../http.service';
import { Raptor } from '../raptor';


@Component({
  selector: 'app-show',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.css']
})
export class ShowComponent implements OnInit {
raptors: object
  constructor(private _httpService: HttpService) { }

  ngOnInit() {
    this.getPeeps()
  }

  getPeeps(){
    let observable = this._httpService.getRaptors();
    observable.subscribe(data => {
      this.raptors = data
    })
  }

  onDelete(id){
  console.log("deleting ",id);
  let observable = this._httpService.deleteRaptor(id);
  observable.subscribe()
  this.getPeeps()
  }

}