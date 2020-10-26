from django.db import models

# Create your models here.
# class Destination(models.Model):
#     fname = models.CharField(max_length=50)
#     lname = models.CharField(max_length=20)
#     dob = models.DateField(max_length=8)
#     email = models.EmailField(max_length=50)
#     password = models.CharField(max_length=20)
class cards:
    img: str
    item: str
    desc: str
    price: float