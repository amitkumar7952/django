from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.IntegerField(null=True)
    message=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Services(models.Model):
    service_icon=models.CharField(max_length=200)
    service_title=models.CharField(max_length=200)
    service_desc=models.FileField(upload_to="images",null=True,default=None)
    def __str__(self):
        return self.service_title         
