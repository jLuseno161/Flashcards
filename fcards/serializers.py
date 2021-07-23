from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
import enum

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flashcard
        fields ='name,title,description',
        name =serializers.CharField(max_length=200)
        title = serializers.CharField(max_length=200)
        description =serializers.CharField()
        # category = serializers(Category,on_delete=models.CASCADE,default='0')
      

    def create(self,validated_data):
        return Flashcard.objects.create(name=validated_data['name'],
                                        title=validated_data['title'],
                                        
                                        description=validated_data['description'],)
                                        # category=validated_data['category'],


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user        