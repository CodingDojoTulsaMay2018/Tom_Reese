import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Raptor } from './raptor';




@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private _http: HttpClient) {

   }

   getRaptors(){
     return this._http.get('/raptor');
   } 

   postRaptor(raptor){
    return this._http.post('/raptor', raptor);
  }

  getRaptor(id){    
    return this._http.get('/raptor/'+id);
  }

  putRaptor(id,raptor){
    return this._http.put('/raptor/'+id, raptor);
  }

  deleteRaptor(id){
    return this._http.delete('/raptor/'+id);
  }
}