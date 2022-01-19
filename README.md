# Course-app Simple Flask backend
The Flask app  consists of a simple API with three endpoints:

- `GET '/'`: This is a simple health check, which returns the response 'Hello, Welcome in course app!'. 
- `GET '/courses'`: This will list all courses ordered by its start date.
- `POST '/add_course'`: This will add anew course and require the course name and the start date the defult start date if not given will be today.
- `POST '/edit_course/<int:course_id>'`: This will edit aspecific course data.
## Initial setup
1. Fork this project to your Github account.
2. Locally clone your forked version to begin working on the app.
## Build containers
cd to the app directory and run
```bash
docker-compose up
```
check that there is two containers (one for Flask app and the other for Postgres) are running by
```bash
docker ps -a
```
### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
### Error Handling
Errors are returned as JSON objects in the following format:
```
{"error":404,"message":"resource not found","success":false}
```
The API will return three error types when requests fail:
- 404: Resource Not Found
- 422: Not Processable 
## Endpoints 

GET '/'
-  This is a simple health check, which returns the response 'Hello, Welcome in course app! .
- Request Arguments: None
Sample: ``` curl http://127.0.0.1:5000/```

GET '/courses'
- Returns a list of all courses ordered by its start date .
- Request Arguments: None
Sample: ``` curl http://127.0.0.1:5000/courses```
```
{
  "courses": [
    {
      "id": 3,
      "name": "ff",
      "start_date": "2022-01-15"
    },
    {
      "id": 2,
      "name": "nn",
      "start_date": "2022-01-17"
    }
    {
      "id": 4,
      "name": "gg",
      "start_date": "2022-01-20"
    }
  ]
}
```

POST '/add_course'
- This end point can be used for adding a new course
- JSON request parameters:```{
    'name':  'Arabic',
    'start_date':  '2022-01-20',
}```
- Sample:```curl http://127.0.0.1:5000/add_course -X POST -H "Content-Type: application/json" -d "{ \"name\": \"Arabic\", \"start_date\": \"2022-01-20\"}"```
```{
  "created": 5,
  "date": "2022-01-20",
  "name": "Arabic"
}
```

POST '/edit_course/<int:course_id>'
- This end point can be used for adding a new course
- Request Arguments:course id - integer
- JSON request parameters:```{
    'name':  'Science',
    'start_date':  '2022-01-22',
}```
- Sample:```curl http://127.0.0.1:5000/edit_course/5 -X POST -H "Content-Type: application/json" -d "{ \"name\": \"Science\", \"start_date\": \"2022-01-22\"}"```
```{
   "date": "2022-01-22",
  "name": "Science",
  "updated": 5
}
```
### Authors
Mahmoud M. Shawara
