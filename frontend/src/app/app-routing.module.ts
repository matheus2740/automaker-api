import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from "@angular/router";
import { AutomakersComponent } from "./automakers/automakers.component";
import { AutomakerDetailComponent } from "./automaker-detail/automaker-detail.component";
import { VehicleModelsComponent } from "./vehiclemodels/vehiclemodels.component";
import { VehiclesComponent } from "./vehicles/vehicles.component";
import { VehicleModelsDetailComponent } from "./vehiclemodels-detail/vehiclemodels-detail.component";
import { VehicleDetailComponent } from "./vehicle-detail/vehicle-detail.component";

const routes: Routes = [
  { path: 'automakers', component: AutomakersComponent },
  { path: 'automaker/:id', component: AutomakerDetailComponent },
  { path: 'vehicle-models', component: VehicleModelsComponent },
  { path: 'vehicle-model/:id', component: VehicleModelsDetailComponent },
  { path: 'vehicles', component: VehiclesComponent },
  { path: 'vehicle/:id', component: VehicleDetailComponent },
  { path: '', redirectTo: '/automakers', pathMatch: 'full' },
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
