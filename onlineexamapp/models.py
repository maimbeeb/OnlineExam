from django.db import models

# Create your models here.
class User(models.Model):
    uname = models.CharField(max_length=100)  
    uemail = models.EmailField()  
    upwd = models.CharField(max_length=20)  
    class Meta:  
        db_table = "user"

class UserExam(models.Model):
    eno = models.CharField(max_length=50)  
    uemail = models.EmailField()  
    uname = models.CharField(max_length=100)
    exname = models.CharField(max_length=150)  
    amount = models.IntegerField()
    currency = models.CharField(max_length=10)
    stripetoken = models.TextField()
    charge_response = models.TextField()
    class Meta:  
        db_table = "user_exams"        
