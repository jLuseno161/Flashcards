from rest_framework import serializers
from .models import Category,Flashcard
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
    
class CategorySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Category
        fields = ['id','category_name']

class CardSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    category = CategorySerializer(many=False, read_only=True)


    class Meta:
        model = Flashcard
        fields = ['id','title','user', 'description','category','date']