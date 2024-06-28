import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { IntroComponent } from '../intro/intro.component';
import { SignrecogComponent } from '../signrecog/signrecog.component';

@Component({
  selector: 'app-signlearn',
  standalone: true,
  imports: [RouterLink,IntroComponent,SignrecogComponent],
  templateUrl: './signlearn.component.html',
  styleUrl: './signlearn.component.css'
})
export class SignlearnComponent {

}
