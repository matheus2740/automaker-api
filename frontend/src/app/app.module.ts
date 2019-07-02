import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'


import { AppComponent } from './app.component';
import { AutomakersComponent } from './automakers/automakers.component';
import { VehicleModelsComponent } from './vehiclemodels/vehiclemodels.component';
import { VehiclesComponent } from './vehicles/vehicles.component';
import { AutomakerDetailComponent } from './automaker-detail/automaker-detail.component';
import { AutomakerService } from "./automaker.service";
import { VehicleModelService } from "./vehicle-model.service";
import { VehicleService } from "./vehicle.service";
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from "@angular/common/http";
import { VehicleModelsDetailComponent } from './vehiclemodels-detail/vehiclemodels-detail.component';
import { VehicleDetailComponent } from './vehicle-detail/vehicle-detail.component';


@NgModule({
  declarations: [
    AppComponent,
    AutomakersComponent,
    VehicleModelsComponent,
    VehiclesComponent,
    AutomakerDetailComponent,
    VehicleModelsDetailComponent,
    VehicleDetailComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [
    AutomakerService,
    VehicleModelService,
    VehicleService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
