import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProjectsService {

  constructor(private _http: HttpClient) {
    console.log('Projects service started.....')
  }

  getAllProjects() {
    return this._http.get(`${environment.BASE_URL}projects/`)
  }

  postProject() {
    return this._http.get(`${environment.BASE_URL}projects/`)
  }

  getSingleProject(projectId:number){
    return this._http.get(`${environment.BASE_URL}projects/${projectId}`)
  }

}
