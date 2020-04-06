import { Component } from '@angular/core';
import { MatIconRegistry } from "@angular/material/icon";
import { DomSanitizer } from "@angular/platform-browser";
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { DialogBodyComponent } from './dialog-body/dialog-body.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  defaultElevation = 2;
  raisedElevation = 8;


  constructor(private matIconRegistry: MatIconRegistry, private domSanitizer: DomSanitizer, private  dialog: MatDialog){
    this.matIconRegistry.addSvgIcon(
      `github`,
      this.domSanitizer.bypassSecurityTrustResourceUrl("../assets/github-icon.svg")
    );
  }
  
  title = 'my-app';



  openDialog() {
    const dialogRef = this.dialog.open(DialogBodyComponent);

    dialogRef.afterClosed().subscribe(result => {
      console.log(`Dialog result: ${result}`);
    });
  }

  openGithub(){
    window.open("https://github.com/caillouc/CovBlock", "_blank");
  }
}