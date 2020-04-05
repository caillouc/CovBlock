import { Component, OnInit } from '@angular/core';
import { NewsService } from '../news.service';

@Component({
  selector: 'app-list-news',
  templateUrl: './list-news.component.html',
  styleUrls: ['./list-news.component.css']
})
export class ListNewsComponent implements OnInit {

  public data;
  constructor(private newsService:NewsService) { }

  ngOnInit(): void {
  }
  
  data_requested(){
    this.newsService.fetch_data().subscribe(
      d =>
      {
        console.log(d);
        this.data = d;
      }
    );
    
  }

}
