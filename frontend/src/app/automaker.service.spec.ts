import { TestBed, inject } from '@angular/core/testing';

import { AutomakerService } from './automaker.service';

describe('AutomakerService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [AutomakerService]
    });
  });

  it('should be created', inject([AutomakerService], (service: AutomakerService) => {
    expect(service).toBeTruthy();
  }));
});
