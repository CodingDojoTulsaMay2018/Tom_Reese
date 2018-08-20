import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProductsComponent } from './products/products.component';
import { BrandComponent } from './products/brand/brand.component';
import { CategoryComponent } from './products/category/category.component';
import { ProductsDetailsComponent } from './products/products-details/products-details.component';
import { ReviewsComponent } from './reviews/reviews.component';
import { AuthorComponent } from './reviews/author/author.component';
import { AllComponent } from './reviews/all/all.component';
import { ReviewDetailsComponent } from './reviews/review-details/review-details.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';



const routes: Routes = [
  { path: 'products', component: ProductsComponent, children: [
    { path: 'productdetails/:id', component: ProductsDetailsComponent},
    { path: 'brand/:brand', component: BrandComponent},
    { path: 'category/:cat', component: CategoryComponent}
  ]},
  { path: 'reviews', component: ReviewsComponent, children: [
    { path: 'reviewdetails/:id', component: ReviewDetailsComponent},
    { path: 'author/:id', component: AuthorComponent},
    { path: 'all/:id', component: AllComponent}
  ]},
  { path: '', pathMatch: 'full', redirectTo: '/' },
  { path: '**', component: PagenotfoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
