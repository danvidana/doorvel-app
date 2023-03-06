# doorvel-app

https://doorvel-app.herokuapp.com/api/zip-codes/04260/
doorvel-app is a Python API for dealing with CRUD operations of a postal codes database.

## Development Plan

### 1st stage: MVP
1. [x] Build GET endpoint -- DONE
- Currently using JsonResponse. Need to find out how to use DRF to send only JSON, default sends whole HTML response -- Going to use normal Response class from DRF -- DONE. Using JsonResponse.
2. [x] Create MySQL instance and database schema -- DONE.
- Not using database schema but Django ORM with Models.
3. [x] Save zip codes on MySQL database -- DONE
- ?Create script to add zip codes from CSV to MySQL database -- DONE
4. [x] Create models for zip codes -- DONE
5. [x] Connect Django with MySQL -- DONE
6. [x] Retrieve zip codes from GET Request -- DONE
7. [x] Host app -- DONE
- Hosted on Heroku
8. [x] Host MySQL instance -- DONE
- Hosted on AWS RDS

### 2nd stage: POST Method to add new PCs
### 3rd stage: PUT Method to update existing PCs

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install doorvel-app.

```bash
cd backend
pip install -r requirement.txt
```

## Running the application
```bash
python manage.py runserver
```

## License

[MIT](https://choosealicense.com/licenses/mit/)