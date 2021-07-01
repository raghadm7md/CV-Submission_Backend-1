from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import FloatField
from django.contrib.auth.models import User


class submission (models.Model):
    user_Id=models.ForeignKey(User, related_name="CVprofileSubmission", on_delete=models.CASCADE, null=True)


martialstatuslist=(
    ("Single","Single"),
    ("Married","Married"),
    )

class UserDetials (models.Model):
    submission_id=models.ForeignKey(submission,on_delete=CASCADE)
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    dateOfBirth=models.DateTimeField(auto_now=True)
    MobileNumber=models.IntegerField(null=False, blank=False, unique=True)
    CountryCode=models.IntegerField()
    Email = models.EmailField(max_length=254 ,unique=True)
    Nationality=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    MartialStatus=models.CharField(max_length=50 , choices=martialstatuslist)
    NumberOfDependents=models.IntegerField()
    YearsOfExpereince=models.IntegerField()

class Education (models.Model):
    submission_id=models.ForeignKey(submission,on_delete=CASCADE)
    DegreeTitle=models.CharField(max_length=50)
    University=models.CharField(max_length=100)
    GPA=models.FloatField()

class Attachment (models.Model):
    submission_id=models.ForeignKey(submission,on_delete=CASCADE)
    FileName=models.CharField(max_length=50)
    File=models.FileField(upload_to='documents/')



