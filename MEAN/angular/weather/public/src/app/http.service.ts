import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private _http: HttpClient) {

   }
   getWeather(city){
     return this._http.get(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=imperial&appid=6fb381816186853e07a832b486096e22`).toPromise()
   }
   

}