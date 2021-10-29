import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  isSuccessful = false;
  isSignInFailed = false;
  errorMessage = '';

  constructor(private _http: HttpClient, private route: Router) {
    console.log('Auth service started.....')
  }

  registerUser(username: string, password: string, password_confirm: string): Observable<any> {
    return this._http.post(`${environment.AUTH_URL}register/`, {
      username, password, password_confirm
    }, httpOptions);
  }

  loginUser(login: string, password: string) {
    this._http.post(`${environment.AUTH_URL}login/`, { login, password }).subscribe(response => {
      let token: any = response
      sessionStorage.setItem('token', token['token'])
      this.route.navigate(['projects'])
      this.isSuccessful = true;
      this.isSignInFailed = false;
    }, err => {
      this.errorMessage = err.error.message;
      this.isSignInFailed = true;
    })
  }

  logoutUser() {
    sessionStorage.removeItem('currentUser');
  }
}

