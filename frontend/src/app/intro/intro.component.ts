import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { SignlearnComponent } from '../signlearn/signlearn.component';
import { SignrecogComponent } from '../signrecog/signrecog.component';

@Component({
  selector: 'app-intro',
  standalone: true,
  imports: [RouterLink,SignlearnComponent,SignrecogComponent],
  templateUrl: './intro.component.html',
  styleUrl: './intro.component.css'
})
export class IntroComponent {
  loadPhotoPage() {
    console.log("HI");
  }

  loadCameraPage() {
    console.log("Bye");
  }

  clearResponse() {
    const videoResponse = document.getElementById('videoResponse');
    if (videoResponse) {
      videoResponse.innerHTML = '';
    }
  }

  speakResponse() {
    const videoResponse = document.getElementById('videoResponse');
    if (videoResponse) {
      const text = videoResponse.innerText.trim();
      if (text) {
        const words = text.split(' ');
        words.forEach(word => {
          const utterance = new SpeechSynthesisUtterance(word);
          speechSynthesis.speak(utterance);
        });
      }
    }
  }

}
