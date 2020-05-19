import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SalesService {

  constructor(private httpClient: HttpClient) { }

  public getAllSales() {
    return this.httpClient.get(environment.apiUrl + '/sales/getAllSales');
  }

  public deleteSales(sales_id){
    return this.httpClient.post(environment.apiUrl + '/sales/deleteSales', sales_id);
  }

}
