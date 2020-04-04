import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Component({
  selector: 'app-list-news',
  templateUrl: './list-news.component.html',
  styleUrls: ['./list-news.component.css']
})
export class ListNewsComponent implements OnInit {

  data;
  httpOptions = {
    headers: new HttpHeaders(
      {
        "Access-Control-Allow-Origin": "*"
      }
    )
  }
  constructor(private http:HttpClient) { }

  ngOnInit(): void {
  }

  data_requested(){
    this.http.get<any>("http://localhost:1415/news?blockingPourcentage=100")
    .subscribe(d =>
      {
        window.alert("yo");
        this.data = d;
      }  
    );
    /*this.http.post<any>("http://localhost:1415/news", {"blockingPourcentage":100 })
    .subscribe(d =>
      {
        console.log("received data");
        this.data = d;
      }
    );*/
  }
}
