import { Component, OnInit } from '@angular/core';
import { NewsService } from '../news.service';

@Component({
  selector: 'app-list-news',
  templateUrl: './list-news.component.html',
  styleUrls: ['./list-news.component.css']
})
export class ListNewsComponent implements OnInit {

  public data;
  public sources;
  public spin: Boolean = true;
  constructor(private newsService:NewsService) { }

  ngOnInit(): void {
    this.data_requested();
    this.newsService.set_callback(this.data_requested.bind(this));
  }

  set_spin(b:boolean){
    this.spin = b;
  }

  
  data_requested(){
    this.set_spin(true);
    this.data = null;
    this.newsService.fetch_data().subscribe(  
      d =>
      {
        console.log(d);
        this.data = d;
        this.sources = d.sources;
        this.newsService.set_sources(this.sources)
        this.set_spin(false);
      }
    );
    
  }

}
