from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from users.models import CustomUser

class LoginUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self,data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        
        raise serializers.ValidationError({'error':"Invalid details."})


class RegisteringUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True, 'min_length':8}}
    
    def validate_password(self, data):
        user = CustomUser(**self.initial_data)
        # password = data.get('password')
        errors = dict()

        try:
            validate_password(data, user)
        except ValidationError as e:
            raise ValidationError(list(e.messages))
        
        return super(RegisteringUserSerializer, self).validate(data)
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user


class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
    

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, trim_whitespace=False)
    new_password = serializers.CharField(requried=True, trim_whitespace=False)

    



