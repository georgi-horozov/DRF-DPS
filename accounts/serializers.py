from rest_framework import serializers
from rest_framework.validators import ValidationError

from .models import CustomUserModel


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ["email", "password"]

    def validate(self, attrs):
        email_exists = CustomUserModel.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("This email already exists")
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)

        user.save()
        return user
