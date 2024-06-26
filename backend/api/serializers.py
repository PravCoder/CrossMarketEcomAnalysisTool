from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True) # defined as string and write-only which means it can only be used during write operations like registration/update

    # meta-class specifies the model-class that is associated with this serializer, set to User-model, can specify the list of fields that will be included in serialization or all fields
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'password'

    # handles creating a new user on registration, takes in dictionary of valid-form-data, returns created-user-obj
    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        print("DOES THIS EVERY GET PRINTED")
        new_user = User(email=email, username=email,  password=password, first_name=first_name, last_name=last_name)  # create new user-obj using form-fields, set username=email, becauwe it is not in the form
        new_user.set_password(password)             # hash the plain-text password before saving to users.password in db
        new_user.save()
        print("\nDOES THIS EVERY GET PRINTED"+str(new_user))
        return new_user
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'UPC', 'website', 'url']  # Fields to include in the serialized output
    
