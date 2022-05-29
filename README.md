# drf_firebase_docker
This repo aimed to integration with firebase and create API endpoint for Auth steps.

---

## Prerequisties

Steps:

- You should create project in your firebase via google console
- Download project credentials as json file
- Set **FIREBASE_WEB_API_KEY** as env variable 

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
  - returns: *credentials for requesting to server(idToken included)*
  - auth token required: **False**
- Sign In to server
  - route: *'/sign-in'*
  - method: **POST**
  - request body: *{"email": "your_email", "password": "your_pwd"}*
  - returns: *credentials for requesting to server(idToken included)*
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

Auth steps:
- Token provided:
  - Get Token from **HTTP_AUTHORIZATION** header
  - Verify id token

## Docker
