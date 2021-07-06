from rest_framework import routers
from .api import  submissionViewSet, UserDetialsViewSet, EducationViewSet, AttachmentViewSet
from .api import RegisterAPI , UserAPI
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path 

router=routers.DefaultRouter()
router.register('api/Submission',submissionViewSet,'CVprofileSubmission')
router.register('api/UserDetial',UserDetialsViewSet,'CVprofileSubmission')
router.register('api/Education',EducationViewSet,'CVprofileSubmission')
router.register('api/Attachment',AttachmentViewSet,'CVprofileSubmission')


urlpatterns = [  
    path('api-token-auth/register', RegisterAPI.as_view()),
    path('api-token-auth/auth', obtain_auth_token),
    path('api-token-auth/user', UserAPI.as_view()),
]

urlpatterns += router.urls