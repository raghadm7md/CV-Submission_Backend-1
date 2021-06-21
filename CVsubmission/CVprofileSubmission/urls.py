from django.conf.urls import url
from rest_framework import routers
from .api import UserViewSet, submissionViewSet, UserDetialsViewSet, EducationViewSet, AttachmentViewSet

router=routers.DefaultRouter()
router.register('api/User',UserViewSet,'CVprofileSubmission')
router.register('api/Sumission',submissionViewSet,'CVprofileSubmission')
router.register('api/UserDetial',UserDetialsViewSet,'CVprofileSubmission')
router.register('api/Education',EducationViewSet,'CVprofileSubmission')
router.register('api/Attachment',AttachmentViewSet,'CVprofileSubmission')

urlpatterns=router.urls
