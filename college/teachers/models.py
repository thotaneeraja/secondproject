from django.db import models
class details(models.Model):
    name=models.CharField(max_length=20)

    address=models.TextField()
    phonenumber=models.BigIntegerField(null=True)


    def __str__(self):
        return self.name



    #gender=models.BooleanField(default=None)



# Create your models here.
