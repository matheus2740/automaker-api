import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Automaker } from '../automaker';
import { AutomakerService } from "../automaker.service";

@Component({
  selector: 'app-automaker-detail',
  templateUrl: './automaker-detail.component.html',
  styleUrls: ['./automaker-detail.component.css']
})
export class AutomakerDetailComponent implements OnInit {

  @Input() automaker: Automaker;

  isNew : boolean = false;

  constructor(
    private route: ActivatedRoute,
    private automakerService: AutomakerService,
    private location: Location
  ) { }

  ngOnInit() {
    this.getAutomaker();
  }

  save(): void {
    if (this.isNew) {
      this.automakerService.createAutomaker(this.automaker)
          .subscribe(() => this.location.back());
    }
    else {
      this.automakerService.updateAutomaker(this.automaker)
          .subscribe(() => this.location.back());
    }
  }

  getAutomaker(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id == 'new') {
      this.automaker = {
        id: null,
        name: '',
        country: ''
      };
      this.isNew = true;
    }
    else {
      this.automakerService.getAutomaker(+id)
          .subscribe(automaker => this.automaker = automaker);
    }

  }

}
