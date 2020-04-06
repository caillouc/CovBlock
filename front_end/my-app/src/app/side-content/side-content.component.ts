import { Component, OnInit} from '@angular/core';
import { NewsService } from '../news.service';
import {FormControl} from '@angular/forms';

@Component({
  selector: 'app-side-content',
  templateUrl: './side-content.component.html',
  styleUrls: ['./side-content.component.css']
})
export class SideContentComponent implements OnInit {

  showExeptions = false;
  sources = {id:"nothhing", name:"Nothing"};
  constructor(private newsService : NewsService) { }

  ngOnInit(): void {
    this.newsService.set_callback2(this.updateSourcesSide.bind(this));
    this.sources = this.newsService.get_sources();
  }

  updateSourcesSide(newSources){
    this.sources = newSources;
  }

  changedAPI(value){
    this.showExeptions = value.value === "nyt" ? false : true;
    this.newsService.change_api(value);
  }

  changedPourcentage(value){
    this.newsService.change_pourcentage(value);
  }

  changedCountry(value){
    this.newsService.change_country(value);
  }

  changedCategorie(value){
    this.newsService.change_categorie(value);
  }

  changedException(value) {
    this.newsService.change_exception(value);
  }

  toppings = new FormControl();
  toppingList: string[] = ['Extra cheese', 'Mushroom', 'Onion', 'Pepperoni', 'Sausage', 'Tomato'];
}
