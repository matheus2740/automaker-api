# RATIONALE

This repository implements a basic REST api and db for managing automobile makers.
It consists of a CRUD backend application for automobile cataloging, as well as an API consumer frontend.
The backend application was implemented in Python and Django, and provides a RESTful API automobile/model/automaker, and a frontend, developed in Angular 5 and TypeScript, providing a very simple CRUD api consumer.

**I have remarked, at the end of this document, ways to improve and complement the application.**

# SETUP:

### Backend
1. Setup a virtualenv with python 3.6 or greater
2. Install the project dependencies
3. `pip install -r requirements.txt`
4. Migrate the database
5. `python manage.py migrate`
6. Fill the local database (SQLite) with fake data, for testing
7. `python manage.py populate_fake_data`
8. Run the django local server
9. `python manage.py runserver 8000`

### Frontend
1. Install Node.js and NPM
2. Install Angular CLI
3. `npm install -g @angular/cli`


# USAGE:

### API

The API is a very simple REST interface, with 3 resources:
* `/api/vehicles/` - for accessing Vehicle objects
* `/api/vehiclemodels` - for accessing VehicleModel objects
* `/api/automakers/` - for accessing Automaker objects

You can browse the API via the integrated Django-REST-Framework API browser, by going to the following address in your browser:

`http://localhost:8000/api/`

NOTE: Endpoint documentation is available under docs/.

### FROTEND

1. Run the local server
2. `cd frontend`
3. `npm start`

Access the UI:

`http://localhost:4200/`

# API DOCUMENTATION

API Documentation for this project is available in two forms:

* The Django REST Framework Browseable API

Go to `http://localhost:8000/api/`.

* API Blueprint doc.

The API Blueprint is a format for specifying APIs, available as a superset of markdown. Any markdown rendered should be able to read the doc, but for best results use the NPM package `aglio`.

A pre-rendered version is also available as HTML (docs/docs.html).

# CODING, FRAMEWORK AND STYLE NOTES:

* I have configured my editor's PEP to a line width of 150 (vs the default 80).
* Python 3.6 and Django 2.0 were chosen, as they are the most up-to-date releases.
* Django-REST-Framework was chosen as the API lib.
* django-filters was chosen to allow filtering of the endpoints, and seamless integration with DRF.
* API Blueprint was chosen as the documentation format for API.
* Angular 5 + TypeScript was chosen for the frontend, as it is the most up-to-date version.

# FIXTURE (FAKE DATA) GENERATION

A simple random approach was used for data generation.
Most names are either random words (generated via a random word generator), or combination of substantives and adjectives (for the automakers's names).
By default, 10 Automakers, 50 VehicleModels, and 200 Vehicles will be generated

# RUNNING THE TEST SUITE AND COVERAGE REPORT
```
python manage.py test
```

The above command will execute the test suite, and also print a coverage report.

# IMPROVEMENTS (NOT IMPLEMENTED IN THIS POC)

* Pagination of API results, and infinite scroll on frontend
* Never return sequential PKs to client. Use a UUID or other random-generated alphanumeric string as main identifier.
* Expand test suite to cover more corner cases and authentication.
* Cache common results, and signal for expiry, as needed.
* Create a Makefile for automatic docs generation, and automatic test running.
* Create a Dockerfile and integrate Docker for build reproducibility and dev ease of use.
* Implement/enable image upload for VehicleModel.stock_photo and Vehicle.vanity_photo
* Improve UI/UX: Better styles, display images, grid displays (instead of lists)
* Separate repos into frontend and backend

