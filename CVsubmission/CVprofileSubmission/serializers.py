from rest_framework import serializers
from .models import submission , UserDetials ,Education ,Attachment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from django.core.mail import send_mail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
    extra_kwargs = {'password': {'write_only': True}}


  def create(self, validated_data):
      user = User.objects.create_user(username=validated_data['username'],
                                            email=validated_data['email'],
                                            password=validated_data['password'],
                                            first_name=validated_data['first_name'],
                                            last_name=validated_data['last_name'])    
      subject = 'welcome to our website'
      message = f'Hi {user.username}, thank you for registering in CV-profile cubmission.'
      email_from = settings.EMAIL_HOST_USER
      recipient_list = [user.email]
      send_mail( subject, message, email_from, recipient_list )
      return user

class LoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField()

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Incorrect Credentials")

class submissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = submission
        fields = '__all__'

class UserDetialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetials
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

