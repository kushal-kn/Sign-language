import {
  ChangeDetectorRef,
  Component,
  ElementRef,
  ViewChild,
} from '@angular/core';
import { RouterLink } from '@angular/router';
import { SignlearnComponent } from '../signlearn/signlearn.component';
import { IntroComponent } from '../intro/intro.component';

@Component({
  selector: 'app-signrecog',
  standalone: true,
  imports: [RouterLink, SignlearnComponent, IntroComponent],
  templateUrl: './signrecog.component.html',
  styleUrl: './signrecog.component.css',
})
export class SignrecogComponent {
  videoResponse: string = '';
  constructor(private cdr: ChangeDetectorRef) {}

  ngOnInit(): void {
    this.loadCameraPage();
  }

  clearResponse(): void {
    const videoResponseElement = document.getElementById('videoResponse');
    if (videoResponseElement) {
      videoResponseElement.textContent = ''; // Clear the content of the element
    }
  }

  loadCameraPage(): void {
    const video = document.getElementById('video') as HTMLVideoElement;
    const recordButton = document.getElementById(
      'recordButton'
    ) as HTMLButtonElement;

    let stream: MediaStream;
    let mediaRecorder: MediaRecorder;
    let chunks: BlobPart[] = [];
    let isRecording = false;

    // Access webcam
    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((mediaStream) => {
        video.srcObject = mediaStream;
        stream = mediaStream;
      })
      .catch((err) => {
        console.error('Error accessing webcam:', err);
      });

    // Declare functions
    const toggleRecording = () => {
      if (!isRecording) {
        startRecording();
        recordButton.textContent = 'Stop Recording';
      } else {
        stopRecording();
        recordButton.textContent = 'Start Recording';
      }
      isRecording = !isRecording;
    };

    const startRecording = () => {
      mediaRecorder = new MediaRecorder(stream);

      mediaRecorder.ondataavailable = (event: BlobEvent) => {
        chunks.push(event.data);
      };

      mediaRecorder.onstop = () => {
        const blob = new Blob(chunks, { type: 'video/webm' });
        const formData = new FormData();
        formData.append('video', blob, 'recorded_video.webm'); // ✅ Explicit filename

        fetch('http://127.0.0.1:5000/predict', {
          method: 'POST',
          body: formData,
        })
          .then((response) => response.json())
          .then((data) => {
            console.log('Response', data);

            const responseEl = document.getElementById('videoResponse');
            if (responseEl) {
              if (data.status === 'success') {
                responseEl.textContent += ` ${data.recognizedSign}`;
              } else {
                responseEl.textContent += ` ${
                  data.message || 'An error occurred'
                }`;
              }
            }
          })
          .catch((error) => {
            console.error('Error sending video to API:', error);
          });

        chunks = []; 
      };

      mediaRecorder.start();
    };

    const stopRecording = () => {
      if (mediaRecorder && mediaRecorder.state === 'recording') {
        mediaRecorder.stop();
      }
    };

    // Event listeners
    recordButton.addEventListener('click', toggleRecording);
    recordButton.addEventListener('mouseleave', stopRecording);
  }
  speakResponse() {
    const videoResponseElement = document.getElementById('videoResponse');
    if (videoResponseElement) {
      const text = videoResponseElement.innerText.trim();
      if (text) {
        const utterance = new SpeechSynthesisUtterance(text);
        speechSynthesis.speak(utterance);
      }
    } else {
      console.error("Element with ID 'videoResponse' not found.");
    }
  }
}
