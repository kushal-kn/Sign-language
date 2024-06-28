import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SignlearnComponent } from './signlearn/signlearn.component';
import { SignrecogComponent } from './signrecog/signrecog.component';
import { IntroComponent } from './intro/intro.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,CommonModule,SignlearnComponent,SignrecogComponent,IntroComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  
}
