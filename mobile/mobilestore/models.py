from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    pnumber=models.IntegerField(max_length=10)
    message=models.CharField(max_length=200)
    def str(self):
        return self.email
class Services(models.Model):
    service_icon= models.CharField(max_length=200)
    service_title= models.CharField(max_length=200)
    service_desc= models.TextField()
    service_img= models.FileField(upload_to="images", null=True, default=None)
    def str(self):
        return self.service_title
    class login(models.Model):
        UserName=models.CharField(max_length=200)
        Pasword=models.CharField(max_length=50)
        def __str__(self):
            return self.UserName