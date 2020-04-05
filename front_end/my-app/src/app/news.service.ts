import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  private data;
  private api = "google";
  public sources;
  private pourcentage = 100;
  private callback;
  private callback2;
  private exceptions = [];
  private country = "";
  private category = "";
  constructor(private http: HttpClient) { }

  change_api(value){
    console.log(value);
    this.api = value.value;
    this.callback();
  }

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

  change_exception(value){
    console.log(value);
    this.exceptions = value.value;
    this.callback();
  }

  set_callback(f){
    this.callback = f;
  }
  set_callback2(f) {
    this.callback2 = f;
  }

  set_sources(newSources){
    this.sources = newSources;  
    this.callback2(this.sources);
  }

  get_sources(){
    return this.sources;
  }

  fetch_data(){
    return this.http.get<any>("http://localhost:1415/news?blockingPourcentage=" + this.pourcentage.toString() +
    ("&api=" + this.api) + 
    (this.country === "" ? "" : "&country=" + this.country.toString()) +
    (this.category === "" ? "" : "&category=" + this.category.toString()) +
    //TODO change check for empty array
    (this.exceptions.length === 0 ? "" : "&exception=" + this.exceptions.map(s => s + "_").toString().slice(0, -1))
    ) 
  }

  get_data(){
    return this.data;
  }
}
