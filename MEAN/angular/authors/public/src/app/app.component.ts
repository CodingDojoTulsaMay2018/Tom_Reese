import { HttpService } from './http.service';
import { Component, OnInit } from '@angular/core';
import { Author } from './author';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Favorite Authors';
  
  constructor(private _httpService: HttpService){}

  ngOnInit(): void {}


}
