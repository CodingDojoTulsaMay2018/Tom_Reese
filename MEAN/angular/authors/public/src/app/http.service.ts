import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Author } from './author';




@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private _http: HttpClient) {

   }

   getAuthors(){
     return this._http.get('/author');
   } 

   postAuthor(author){
    return this._http.post('/author', author);
  }

  getAuthor(id){    
    return this._http.get('/author/'+id);
  }

  putAuthor(id,author){
    return this._http.put('/author/'+id, author);
  }

  deleteAuthor(id){
    return this._http.delete('/author/'+id);
  }
}