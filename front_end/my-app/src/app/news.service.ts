import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  private data;
  private pourcentage = 100;
  private callback;
  private country = "";
  private category = "";
  constructor(private http: HttpClient) { }

  change_pourcentage(value){
    console.log(value);
    this.pourcentage = value.value;
    this.callback();
  }

  change_categorie(value){
    console.log(value);
    this.category = value.value;
    this.callback();
  }

  change_country(value){
    console.log(value);
    this.country = value.value;
    this.callback();
  }

  set_callback(f){
    this.callback = f;
  }

  fetch_data(){
    return this.http.get<any>("http://localhost:1415/news?blockingPourcentage=" + this.pourcentage.toString() + 
    (this.country === "" ? "" : "&country=" + this.country.toString()) +
    (this.category === "" ? "" : "&category=" + this.category.toString()))
  }

  get_data(){
    return this.data;
  }
}
