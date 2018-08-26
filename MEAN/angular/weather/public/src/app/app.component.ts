import { HttpService } from './http.service';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  // template: `
  // <input #box (keyup.enter)="onEnter(box.value)">
  // <p>{{value}}</p>`
})
export class AppComponent implements OnInit  {
  title = 'public';
  weather
  temp
  high
  low
  avg
  status
  humidity
  check = false
  city = ""

  constructor(
    private _httpService: HttpService,
    private _route: ActivatedRoute,
    private _router: Router
  ){}
  // ngOnInit will run when the component is initialized, after the constructor method.
  ngOnInit(){
    this._route.params.subscribe((params: Params) => {
      console.log(params['id'])
    // this.getWeather()
  });
  }
  
  onEnter(value: string){
    this._router.navigate(['/custom/',value];
    this.check = true  
    )}

  goHome() {
    this._router.navigate(['/home']);
  }

}