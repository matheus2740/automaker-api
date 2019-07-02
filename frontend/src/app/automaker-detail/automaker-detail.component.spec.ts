import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AutomakerDetailComponent } from './automaker-detail.component';

describe('AutomakerDetailComponent', () => {
  let component: AutomakerDetailComponent;
  let fixture: ComponentFixture<AutomakerDetailComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AutomakerDetailComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AutomakerDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
