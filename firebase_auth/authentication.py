import requests
import json

import firebase_admin
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication

from .exceptions import FirebaseError
from .exceptions import InvalidAuthToken
from .exceptions import NoAuthToken

cred = credentials.Certificate(settings.FIREBASE_VARS['CREDENTIALS_PATH'])

default_app = firebase_admin.initialize_app(cred)

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")

        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
            pass

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        try:
            user= User.objects.get(username=uid)
            user.last_login = timezone.localtime()
            return (user, None)

        except Exception:
            print("User not found")
            print("User has no profile")
            return None

    def sign_in_with_email_and_password(self,email, password, return_secure_token=True):
        payload = json.dumps({"email":email, "password":password, "return_secure_token":return_secure_token})
        FIREBASE_WEB_API_KEY = settings.FIREBASE_VARS['FIREBASE_WEB_API_KEY']
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"

        r = requests.post(rest_api_url,
                    params={"key": FIREBASE_WEB_API_KEY},
                    data=payload)

        return r.json()

    def sign_up_with_email_and_password(self,email, password, return_secure_token=True):
        payload = json.dumps({"email":email, "password":password, "return_secure_token":return_secure_token})
        FIREBASE_WEB_API_KEY = settings.FIREBASE_VARS['FIREBASE_WEB_API_KEY']
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"

        r = requests.post(rest_api_url,
                    params={"key": FIREBASE_WEB_API_KEY},
                    data=payload)

        return r.json()