from rest_framework.response import Response
from rest_framework import viewsets , permissions , generics
from django.contrib.auth.models import User
from .models import  submission , UserDetials ,Education ,Attachment
from .serializers import RegisterSerializer ,LoginSerializer, UserSerializer , submissionSerializer , UserDetialsSerializer ,EducationSerializer ,AttachmentSerializer
from knox.models import AuthToken



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = UserSerializer
    def get_object(self):
     return self.request.user

class UserAPI(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticated]
  serializer_class = UserSerializer
  def get_object(self):
    return self.request.user


class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": AuthToken.objects.create(user)[1]
    })

class LoginAPI(generics.GenericAPIView):
  serializer_class = LoginSerializer

  def post(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data
    token = AuthToken.objects.create(user)[1]
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": token
    })

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
    
