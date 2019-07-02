import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { Observable } from "rxjs/Observable";
import { Vehicle } from "./vehicle";

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class VehicleService {

  private url : string = 'http://localhost:8000/api/vehicles/';
  private detailURL : string = 'http://localhost:8000/api/vehicles/';

  constructor(private http: HttpClient) {
  }

  getVehicles(filters: object): Observable<Vehicle[]> {
    let params = new HttpParams();
    for (let key in filters) {
      params = params.set(key, filters[key]);
    }
    return this.http.get<Vehicle[]>(this.url, {params: params})
  }
  getVehicle(id: number): Observable<Vehicle> {
    return this.http.get<Vehicle>(this.detailURL + id)
  }
  updateVehicle (model: Vehicle): Observable<any> {
    return this.http.put(this.detailURL + model.id + '/', model, httpOptions)
  }
  createVehicle (model: Vehicle): Observable<any> {
    return this.http.post(this.url, model, httpOptions)
  }

}
