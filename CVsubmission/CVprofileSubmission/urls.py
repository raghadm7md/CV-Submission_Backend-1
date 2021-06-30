from rest_framework import routers
from .api import UserViewSet, submissionViewSet, UserDetialsViewSet, EducationViewSet, AttachmentViewSet
from .api import RegisterAPI, LoginAPI
from django.urls import path ,include
from knox import views as knox_views




router=routers.DefaultRouter()
router.register('api/User',UserViewSet,'CVprofileSubmission')
router.register('api/Sumission',submissionViewSet,'CVprofileSubmission')
router.register('api/UserDetial',UserDetialsViewSet,'CVprofileSubmission')
router.register('api/Education',EducationViewSet,'CVprofileSubmission')
router.register('api/Attachment',AttachmentViewSet,'CVprofileSubmission')
urlpatterns=router.urls


urlpatterns = [
    path('api-token/auth', include('knox.urls')),
    path('api-token-auth/register', RegisterAPI.as_view()),
    path('api-token-auth/login', LoginAPI.as_view()),
    # path('api-token-auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')

]

