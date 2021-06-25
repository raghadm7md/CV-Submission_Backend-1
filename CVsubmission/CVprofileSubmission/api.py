from rest_framework import viewsets , permissions 
from .models import User , submission , UserDetials ,Education ,Attachment
from .serializers import UserSerializer , submissionSerializer , UserDetialsSerializer ,EducationSerializer ,AttachmentSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = UserSerializer

class submissionViewSet(viewsets.ModelViewSet):
    queryset = submission.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = submissionSerializer

class UserDetialsViewSet(viewsets.ModelViewSet):
    queryset = UserDetials.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = UserDetialsSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = EducationSerializer

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = AttachmentSerializer

