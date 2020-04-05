import { Component, OnInit } from '@angular/core';
import {Input} from '@angular/core';


@Component({
  selector: 'app-article-box',
  templateUrl: './article-box.component.html',
  styleUrls: ['./article-box.component.css']
})
export class ArticleBoxComponent implements OnInit {

  @Input() title;
  @Input() author;
  @Input() source;
  @Input() content;
  @Input() description;
  @Input() link;
  @Input() img;

  constructor() { }

  ngOnInit(): void {
  }

}
