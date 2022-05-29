from rest_framework.response import Response 
from rest_framework.decorators import api_view
from firebase_auth.models import Item
from .serializers import ItemSerializer, UserSerializer
from firebase_auth.authentication import FirebaseAuthentication

fireb_auth = FirebaseAuthentication()

@api_view(['GET'])
def get_item(request):
    if fireb_auth.authenticate(request) is not None:
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    else:
        serializer = {'error': 'Unauthorized'}
        return Response(serializer)

@api_view(['POST'])
def add_item(request):
    if fireb_auth.authenticate(request) is not None:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    else:
        serializer = {'error': 'Unauthorized'}
        return Response(serializer)

@api_view(['POST'])
def sign_in(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        result = fireb_auth.sign_in_with_email_and_password(serializer.data['email'], serializer.data['password'])
        return Response(result)
    else:
        serializer = {'error': 'No signed in user'}
        return Response(serializer)

@api_view(['POST'])
def sign_up(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        result = fireb_auth.sign_up_with_email_and_password(serializer.data['email'], serializer.data['password'])
        return Response(result)
    else:
        serializer = {'error': 'Request body is not valid'}
        return Response(serializer)