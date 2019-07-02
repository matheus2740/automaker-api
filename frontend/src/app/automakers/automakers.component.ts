import { Component, OnInit } from '@angular/core';
import { Automaker } from '../automaker'
import { AutomakerService } from "../automaker.service";

@Component({
  selector: 'app-automakers',
  templateUrl: './automakers.component.html',
  styleUrls: ['./automakers.component.css']
})
export class AutomakersComponent implements OnInit {

  automakers : Automaker[];

  constructor(private automakerService: AutomakerService) { }

  ngOnInit() {
    this.getAutomakers()
  }

  getAutomakers() : void {
    this.automakerService.getAutomakers()
        .subscribe(automakers => this.automakers = automakers);
  }

}
