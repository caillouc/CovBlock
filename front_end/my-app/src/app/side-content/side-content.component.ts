import { Component, OnInit } from '@angular/core';
import { NewsService } from '../news.service';

@Component({
  selector: 'app-side-content',
  templateUrl: './side-content.component.html',
  styleUrls: ['./side-content.component.css']
})
export class SideContentComponent implements OnInit {

  constructor(private newsService : NewsService) { }

  ngOnInit(): void {
    
  }

  changedPourcentage(value){
    this.newsService.change_pourcentage(value);
  }

}
