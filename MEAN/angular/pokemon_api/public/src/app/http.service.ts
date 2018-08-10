import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private _http: HttpClient) {
    this.getPoke();
   }


   getPoke(){
     let bulbasaur = this._http.get('https://pokeapi.co/api/v2/pokemon/143/');
     bulbasaur.subscribe(data => console.log(data))
     bulbasaur.subscribe(data => {for(var i of data["abilities"]){console.log(i.ability.name);}})

     let allpokes = this._http.get('https://pokeapi.co/api/v2/ability/immunity/');
     allpokes.subscribe(data => {for(var i of data["pokemon"]){console.log(i.pokemon["name"])}})
    
  };

}
  

