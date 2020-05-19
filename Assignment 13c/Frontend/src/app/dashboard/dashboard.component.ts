import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth/auth.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})

export class DashboardComponent implements OnInit {

  user: firebase.User;

  constructor(
    private auth: AuthService,
    private router: Router
  ) {
    this.auth.getUserState()
      .subscribe( user => {
        this.user = user;
        if(this.user === undefined || this.user === null){
          this.router.navigate(['/login']);
        }
      })
  }

  ngOnInit() {
  }

}
