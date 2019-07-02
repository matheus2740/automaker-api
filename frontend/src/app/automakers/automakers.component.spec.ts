import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AutomakersComponent } from './automakers.component';

describe('AutomakersComponent', () => {
  let component: AutomakersComponent;
  let fixture: ComponentFixture<AutomakersComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AutomakersComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AutomakersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
