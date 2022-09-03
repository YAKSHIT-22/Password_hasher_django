from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=10)
    #crating modelform using these fields
    class Meta:
        #meta class tells which fields that we want to include in the form from the database table
        db_table = 'Login'