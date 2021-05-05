from django.db import models

# Create your models here.
class Contacts(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    emailid = models.EmailField(max_length=50)
