import { Component, OnInit } from '@angular/core';
import { HttpService } from './../http.service';
import { Author } from './../author';


@Component({
  selector: 'app-show',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.css']
})
export class ShowComponent implements OnInit {
authors: object
  constructor(private _httpService: HttpService) { }

  ngOnInit() {
    this.getPeeps()
  }

  getPeeps(){
    let observable = this._httpService.getAuthors();
    observable.subscribe(data => {
      this.authors = data
    })
  }

  onDelete(id){
  console.log("deleting ",id);
  let observable = this._httpService.deleteAuthor(id);
  observable.subscribe()
  this.getPeeps()
  }

}