import { TestBed, inject } from '@angular/core/testing';

import { VehicleModelService } from './vehicle-model.service';

describe('VehicleModelService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [VehicleModelService]
    });
  });

  it('should be created', inject([VehicleModelService], (service: VehicleModelService) => {
    expect(service).toBeTruthy();
  }));
});
