from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        field = '__all__'
        extra_kwargs = {'password' : {'write-only' : True} }  # kwargs means additional keyword arguments. 
        # We are creating this dictionary to specify that we shouldn't know the password value. When we query on insomnia we wont 
        # get the password value in the response.
        # This is a security measure to ensure that sensitive information like passwords is not exposed in API

    def create (self, validated_data):
        return CustomUser.objects.create_user(**validated_data) # the ** is related to kwargs.
        # This method is used to create a new user instance. It uses the `create_user` method to ensure that the password is hashed.
        