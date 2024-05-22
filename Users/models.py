from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=200)
    username = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    email = models.CharField(max_length=256,null=True,blank=True)
    user_feedback =  models.TextField()


    def __str__(self):
        return self.email