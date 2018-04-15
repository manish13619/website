from django.db import models
 
 
# Create your models here.
 
class Product(models.Model):
    name = models.CharField(max_length=100)
    rollNo = models.CharField(max_length=15)
    mobile = models.CharField(max_length=12)
    complaintType = models.CharField(max_length=10)
    hostelNo = models.CharField(max_length=5)
    wing = models.CharField(max_length=5)
    roomNo = models.CharField(max_length=4)
    complaintTitle = models.CharField(max_length=100)
    complaintDesc = models.CharField(max_length=350)

    def __str__(self):
        return self.rollNo + "_" + str(self.id);
