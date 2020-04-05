import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatToolbarModule} from '@angular/material/toolbar';
import { MatSliderModule } from '@angular/material/slider'; 
import { MatFormFieldModule } from '@angular/material/form-field'; 
import { MatSelectModule } from '@angular/material/select'; 
import { MatCardModule } from '@angular/material/card'; 
import { MatDividerModule } from '@angular/material/divider';
import { MatButtonModule} from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle'; 
import { MatGridListModule } from '@angular/material/grid-list'
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner'; 
import { ReactiveFormsModule } from '@angular/forms';

//Nos composants
import { SideContentComponent } from './side-content/side-content.component';
import { ListNewsComponent } from './list-news/list-news.component';
import { ArticleBoxComponent } from './list-news/article-box/article-box.component';

@NgModule({
  declarations: [
    AppComponent,
    SideContentComponent,
    ListNewsComponent,
    ArticleBoxComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatIconModule,
    MatToolbarModule,
    MatSliderModule,
    MatFormFieldModule,
    MatSelectModule,
    HttpClientModule,
    MatCardModule,
    MatDividerModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatGridListModule,
    MatProgressSpinnerModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
