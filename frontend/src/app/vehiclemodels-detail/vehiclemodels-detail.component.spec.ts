import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { VehicleModelsDetailComponent } from './vehiclemodels-detail.component';

describe('VehicleModelsDetailComponent', () => {
  let component: VehicleModelsDetailComponent;
  let fixture: ComponentFixture<VehicleModelsDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ VehicleModelsDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(VehicleModelsDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
