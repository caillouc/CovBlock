import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  private data;
  private pourcentage = 100;
  constructor(private http: HttpClient) { }

  change_pourcentage(value){
    this.pourcentage = value.value;
  }

  fetch_data(){
    return this.http.get<any>("http://localhost:1415/news?blockingPourcentage=" + this.pourcentage.toString() + "&country=fr")
  }

  get_data(){
    return this.data;
  }
}
