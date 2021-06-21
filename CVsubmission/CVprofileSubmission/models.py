from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import FloatField

# Create your models here.
class User (models.Model):
    # user_Id=models.CharField(max_length=50 , primary_key=True)
    username=models.CharField(max_length=50 , unique=True)
    password=models.CharField(max_length=10)


class submission (models.Model):
    # submission_id=models.CharField(max_length=50, primary_key=True)
    user_Id=models.ForeignKey(User, on_delete=models.CASCADE)


martialstatuslist=(
    ("Single","Single"),
    ("Married","Married"),
    )

class UserDetials (models.Model):
    submission_id=models.ForeignKey(submission,on_delete=CASCADE)
    FirstName=models.CharField(max_length=50)
    LastNmae=models.CharField(max_length=50)
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
    # Education_id=models.CharField(max_length=50,primary_key=True)
    DegreeTitle=models.CharField(max_length=50)
    University=models.CharField(max_length=100)
    GPA=models.FloatField()

class Attachment (models.Model):
    submission_id=models.ForeignKey(submission,on_delete=CASCADE)
    # Attachment_id=models.CharField(max_length=50,primary_key=True)
    FileName=models.CharField(max_length=50)
    File=models.FileField(upload_to='documents/')



