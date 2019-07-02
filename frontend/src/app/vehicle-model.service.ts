import { Injectable } from '@angular/core';

import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs/Observable";
import {VehicleModel} from "./vehiclemodel";

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class VehicleModelService {

  private url : string = 'http://localhost:8000/api/vehiclemodels/';
  private detailURL : string = 'http://localhost:8000/api/vehiclemodels/';

  constructor(private http: HttpClient) {
  }

  getModels(): Observable<VehicleModel[]> {
    return this.http.get<VehicleModel[]>(this.url)
  }
  getModel(id: number): Observable<VehicleModel> {
    return this.http.get<VehicleModel>(this.detailURL + id)
  }
  updateModel (model: VehicleModel): Observable<any> {
    return this.http.put(this.detailURL + model.id + '/', model, httpOptions)
  }
  createModel (model: VehicleModel): Observable<any> {
    return this.http.post(this.url, model, httpOptions)
  }

}
