import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Automaker } from './automaker';
import { Observable } from 'rxjs/Observable';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class AutomakerService {

  private url : string = 'http://localhost:8000/api/automakers/';
  private detailURL : string = 'http://localhost:8000/api/automakers/';

  constructor(private http: HttpClient) {
  }

  getAutomakers(): Observable<Automaker[]> {
    return this.http.get<Automaker[]>(this.url)
  }
  getAutomaker(id: number): Observable<Automaker> {
    return this.http.get<Automaker>(this.detailURL + id)
  }
  updateAutomaker (automaker: Automaker): Observable<any> {
    return this.http.put(this.detailURL + automaker.id + '/', automaker, httpOptions)
  }
  createAutomaker (automaker: Automaker): Observable<any> {
    return this.http.post(this.url, automaker, httpOptions)
  }

}
