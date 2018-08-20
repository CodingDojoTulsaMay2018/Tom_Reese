import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
@Component({
  selector: 'app-products-details',
  templateUrl: './products-details.component.html',
  styleUrls: ['./products-details.component.css']
})
export class ProductsDetailsComponent implements OnInit {
  number: number
  constructor(
    private _route: ActivatedRoute,
    private _router: Router
  ) {}

  ngOnInit(){
      this._route.params.subscribe(params => {
        console.log(params['id']);
        this.number = params['id']
      });
  }

}
