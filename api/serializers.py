from rest_framework import serializers 
from firebase_auth.models import Item, UserPayload

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayload
        fields = '__all__'