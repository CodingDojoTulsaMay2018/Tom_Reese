import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { HttpService } from './http.service';
import { FormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';

import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { EditComponent } from './edit/edit.component';
import { ShowComponent } from './show/show.component';
import { NewComponent } from './new/new.component';
import { AppComponent } from './app.component';



@NgModule({
  declarations: [
    AppComponent,
    PagenotfoundComponent,
    NewComponent,
    EditComponent,
    ShowComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [HttpService],
  bootstrap: [AppComponent]
})
export class AppModule { }