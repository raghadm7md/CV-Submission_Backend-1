from rest_framework import serializers
from .models import User , submission , UserDetials ,Education ,Attachment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

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
