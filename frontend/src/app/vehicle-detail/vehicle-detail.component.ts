import {Component, Input, OnInit} from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Location} from "@angular/common";
import {Vehicle} from "../vehicle";
import {VehicleService} from "../vehicle.service";

@Component({
  selector: 'app-vehicle-detail',
  templateUrl: './vehicle-detail.component.html',
  styleUrls: ['./vehicle-detail.component.css']
})
export class VehicleDetailComponent implements OnInit {

  @Input() vehicle: Vehicle;

  isNew : boolean = false;

  constructor(
    private route: ActivatedRoute,
    private vehicleService: VehicleService,
    private location: Location
  ) { }

  ngOnInit() {
    this.getAutomaker();
  }

  save(): void {
    if (this.isNew) {
      this.vehicleService.createVehicle(this.vehicle)
          .subscribe(() => this.location.back());
    }
    else {
      this.vehicleService.createVehicle(this.vehicle)
          .subscribe(() => this.location.back());
    }
  }

  getAutomaker(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id == 'new') {
      this.vehicle = {
        id: null,
        model: {
          name: '',
          automaker_name: ''
        },
        model_id: null,
        mileage: null,
        engine_volume: null,
        color: '',
        vanity_photo: ''
      };
      this.isNew = true;
    }
    else {
      this.vehicleService.getVehicle(+id)
          .subscribe(vehicle => this.vehicle = vehicle);
    }

  }

}
