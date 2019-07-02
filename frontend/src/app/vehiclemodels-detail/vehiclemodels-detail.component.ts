import {Component, Input, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Location} from "@angular/common";
import {VehicleModel} from "../vehiclemodel";
import {VehicleModelService} from "../vehicle-model.service";

@Component({
  selector: 'app-vehiclemodels-detail',
  templateUrl: './vehiclemodels-detail.component.html',
  styleUrls: ['./vehiclemodels-detail.component.css']
})
export class VehicleModelsDetailComponent implements OnInit {

  @Input() vModel: VehicleModel;

  isNew : boolean = false;

  constructor(
    private route: ActivatedRoute,
    private vehicleModelService: VehicleModelService,
    private location: Location
  ) { }

  ngOnInit() {
    this.getModels();
  }

  save(): void {
    if (this.isNew) {
      this.vehicleModelService.createModel(this.vModel)
          .subscribe(() => this.location.back());
    }
    else {
      this.vehicleModelService.updateModel(this.vModel)
          .subscribe(() => this.location.back());
    }
  }

  getModels(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id == 'new') {
      this.vModel = {
        id: null,
        name: '',
        vehicle_type: null,
        automaker: null,
        automaker_name: '',
        stock_photo: ''
      };
      this.isNew = true;
    }
    else {
      this.vehicleModelService.getModel(+id)
          .subscribe(vModel => this.vModel = vModel);
    }

  }

}
