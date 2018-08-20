import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private _http: HttpClient) {
    this.getFrisbees();
   }

   getFrisbees(){
     return this._http.get('/frisbees');
   }

   postFrisbees(frisbee){
    return this._http.post('/frisbees', frisbee);
  }

  getFrisbee(id){
    return this._http.get('/frisbees/'+id);
  }

  putFrisbees(id,frisbee){
    return this._http.put('/frisbees/'+id, frisbee);
  }

  deleteFrisbee(id){
    return this._http.delete('/frisbees/'+id);
  }
  rateFrisbees(frisbee){
    return this._http.post('/frisbees/'+frisbee.id, frisbee);
  }
}