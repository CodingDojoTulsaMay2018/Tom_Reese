import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { TaskComponent } from './task/task.component';


const routes: Routes = [
  { path: 'task', component: TaskComponent },
  { path: 'task/:id', component: TaskComponent },
  { path: '', pathMatch: 'full', redirectTo: '/task' },
  { path: '**', component: PagenotfoundComponent }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
