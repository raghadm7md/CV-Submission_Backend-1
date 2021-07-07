from rest_framework.response import Response
from rest_framework import viewsets , permissions , generics, authentication
from django.contrib.auth.models import User
from django.contrib.auth import logout
from rest_framework import status
from .models import  submission , UserDetials ,Education ,Attachment
from .serializers import RegisterSerializer ,LoginSerializer, UserSerializer , submissionSerializer , UserDetialsSerializer ,EducationSerializer ,AttachmentSerializer
# from knox.models import AuthToken

from rest_framework.authtoken.models import Token
from django.shortcuts import get_list_or_404, get_object_or_404


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = UserSerializer
    def get_object(self):
     return self.request.user

class UserAPI(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticated]
  authentication_classes = (authentication.TokenAuthentication,)
  serializer_class = UserSerializer


  def get(self,request):
      return Response({
          "user":UserSerializer(request.user).data,
      })


class RegisterAPI(generics.GenericAPIView):
  serializer_class = RegisterSerializer

  def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    return Response({
      "user": UserSerializer(user, context=self.get_serializer_context()).data,
      "token": Token.objects.create(user)[1]
    })

class LoginAPI(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data
      token = Token.objects.create(user)[1]
      return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": token
      })
      
class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
      logout(request)
      data = {'success': 'Sucessfully logged out'}
      return Response(data=data, status=status.HTTP_200_OK)

class submissionViewSet(viewsets.ModelViewSet):
    queryset = submission.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = submissionSerializer

    def list(self, request):
        queryset = submission.objects.filter(user_Id=request.user.id)
        serializer = submissionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = submission.objects.create(user_Id=request.user)
        serializer = submissionSerializer(queryset)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = submission.objects.filter(user_Id=request.user.id)
        object = get_object_or_404(queryset, pk=pk)
        serializer = submissionSerializer(object)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = submission.objects.filter(user_Id=request.user.id)
        object = get_object_or_404(queryset, pk=pk)
        # This is ust an example for an update
        # Link submission to another user
        object.user_Id = User.objects.get(id=request.data['id'])
        object.save()
        serializer = submissionSerializer(object)
        return Response(serializer.data)


class UserDetialsViewSet(viewsets.ModelViewSet):
    queryset = UserDetials.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = UserDetialsSerializer

    def list(self, request):
        queryset = UserDetials.objects.filter(submission_id__user_Id=request.user.id)
        serializer = UserDetialsSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, pk=None):
        queryset = UserDetials.objects.filter(submission_id__user_Id=request.user.id)
        object = get_object_or_404(queryset, pk=pk)
        serializer = UserDetialsSerializer(object)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = UserDetials.objects.filter(submission_id__user_Id=request.user.id)
        object = get_object_or_404(queryset, pk=pk)
        object.submission_id__user_Id = User.objects.get(id=request.data['id'])
        object.save()
        serializer = UserDetialsSerializer(object)
        return Response(serializer.data)


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = EducationSerializer

    def list(self, request):
        queryset = Education.objects.filter(submission_id__user_Id=request.user.id)
        serializer = EducationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Education.objects.filter(submission_id__user_Id=request.user.id)
        object = get_object_or_404(queryset, pk=pk)
        serializer = EducationSerializer(object)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Education.objects.filter(submission_id__user_Id=request.user.id)
        object = get_object_or_404(queryset, pk=pk)
        object.submission_id__user_Id = submission.objects.get(id=request.data['id'])
        object.save()
        serializer = EducationSerializer(object)
        return Response(serializer.data)

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    permissions_class =[permissions.IsAuthenticated] 
    serializer_class = AttachmentSerializer

    def list(self, request):
        queryset = Attachment.objects.filter(submission_id__user_Id=request.user.id)
        serializer = AttachmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Attachment.objects.filter(submission_id__user_Id=request.user.id)
        object = get_object_or_404(queryset, pk=pk)
        serializer = AttachmentSerializer(object)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Attachment.objects.filter(submission_id__user_Id=request.user.id)
        object = get_object_or_404(queryset, pk=pk)
        object.submission_id__user_Id = submission.objects.get(id=request.data['id'])
        object.save()
        serializer = AttachmentSerializer(object)
        return Response(serializer.data)
    
