import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class HttpService {
  constructor(private _http: HttpClient) {}
   getAnimals(){
     return this._http.get('/animals')
  }
  postAnimals(newAnimal){
    return this._http.post('/animals', newAnimal)
 }
  showAnimals(id){
  return this._http.get('/animals/'+id)
}
}
  

