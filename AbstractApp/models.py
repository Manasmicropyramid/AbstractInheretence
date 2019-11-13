from django.db import models

class CommonFieds(models.Model):
    email=models.EmailField(max_length=50)
    mobile=models.BigIntegerField()
    location=models.CharField(max_length=50)
    salary=models.IntegerField()

    class Meta:
        abstract=True

class Father(CommonFieds):
    fname=models.CharField(max_length=100)

class Mother(CommonFieds):
    mname=models.CharField(max_length=100)

class Son(CommonFieds):
    sname=models.CharField(max_length=100)
