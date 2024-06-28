import { Routes } from '@angular/router';
import { IntroComponent } from './intro/intro.component';
import { SignlearnComponent } from './signlearn/signlearn.component';
import { SignrecogComponent } from './signrecog/signrecog.component';

export const routes: Routes = [
    {'path':'', component:IntroComponent},
    {'path':'signlearn', component:SignlearnComponent},
    {'path':'signrecog', component:SignrecogComponent},
];
