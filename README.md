# drf_firebase_docker
Django Rest Framework Firebase Authentication Backend with Docker

---

## Prerequisties

Steps:

- You should create project in your firebase via google console
- Download project credentials as json file
- Set **FIREBASE_WEB_API_KEY** as env variable (if you initialize project with Docker you don't need to set it)

---

## Django Rest Framework
There are two models for accessing:
- Item
  - It contains simple item name and name created time
- User
  - It contains email and password for Firebase Auth

Also there are two serailizers for these models.

---
##### API endpoints
- Get all items:
  - route: *'/'*
  - method: **GET**
  - request body: *None*
  - returns: *all items in database*
  - auth token required: **True**
- Add new item:
  - route: *'/add'*
  - method: **POST**
  - request body: *{"name": "item_name"}*
  - returns: *payload which you posted*
  - auth token required: **True**
- Sign Up to server
  - route: *'/sign-up'*
  - method: **POST**
  - request body: *{"email": "your_email", "password": "your_pwd"}*
  - returns: *{"access_token": "<your_access_token>"}*
  - auth token required: **False**
- Sign In to server
  - route: *'/sign-in'*
  - method: **POST**
  - request body: *{"email": "your_email", "password": "your_pwd"}*
  - returns: *{"access_token": "<your_access_token>"}*
  - auth token required: **False**

*NOTE:* If your session is expired, you should sign in again.

---

## Firebase Auth

API steps:
- Sign Up:
  - Create new user in firebase
  - Create new user in database
  - Return credentials for requesting to server(idToken included)
- Sign In:
  - Check user in firebase
  - Check user in database
  - Return credentials for requesting to server(idToken included)
- Add item:
  - Check user in database
  - Add new item to database
  - Return payload which you posted
- Get items:
  - Check user in database
  - Return all items in database
----

## Docker

#### Initialize project with Docker

##### You should configure all the steps below:
- Configure your ***firebase_credentials.json*** file
- Set your **FIREBASE_WEB_API_KEY** from **Dockerfile** as ENV var
- Configure **ADMIN_EMAIL** and **ADMIN_PASSWORD** from *settings.py*
- Build an image *(check from docker-commands.txt)*
- Run container *(check from docker-commands.txt)*

It will be started automatically when you satisfy last step.
If your project started successfully, you can see it in your browser from *http://localhost:8000/*

ATTENTION: You should configure your firebase_credentials.json file in your project root directory. Initially it creates admin user in localhost. You have to sign in with that admin user to firebase project console