import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-list-news',
  templateUrl: './list-news.component.html',
  styleUrls: ['./list-news.component.css']
})
export class ListNewsComponent implements OnInit {

  data;
  constructor(private http:HttpClient) { }

  ngOnInit(): void {
  }

  data_requested(){
    this.http.get<any>("http://localhost:1415/news?blockingPourcentage=100")
    .subscribe(d =>
      {
        console.log(d.articles[0].description);
        this.data = d;
      }  
    );
  }
}
