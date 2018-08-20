import { Component, OnInit } from '@angular/core';
import { HttpService } from './../http.service';

@Component({
  selector: 'app-sanjose',
  templateUrl: './sanjose.component.html',
  styleUrls: ['./sanjose.component.css']
})
export class SanjoseComponent implements OnInit {
  weather
  temp
  high
  low
  avg
  status
  humidity

  constructor(private _httpService: HttpService) { }

  ngOnInit() {
    this.weather = this._httpService.getWeather('san jose').then(weather => {
    this.humidity = weather['main']['humidity']
    this.avg = weather['main']['temp']
    this.high = weather['main']['temp_max']
    this.low = weather['main']['temp_min']
    this.status = weather['weather'][0]['description']
    })
  }

}
