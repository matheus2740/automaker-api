import { Component, OnInit } from '@angular/core';
import { VehicleModelService } from "../vehicle-model.service";
import { VehicleModel } from "../vehiclemodel";

@Component({
  selector: 'app-vehiclemodels',
  templateUrl: './vehiclemodels.component.html',
  styleUrls: ['./vehiclemodels.component.css']
})
export class VehicleModelsComponent implements OnInit {

  vModels : VehicleModel[];

  constructor(private vehicleModelService: VehicleModelService) { }

  ngOnInit() {
    this.getModels()
  }

  getModels() : void {
    this.vehicleModelService.getModels()
        .subscribe(vModels => this.vModels = vModels);
  }

}
