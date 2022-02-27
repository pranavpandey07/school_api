from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class preschool(models.Model):
    School_id=models.AutoField(blank=False,primary_key = True)
    Name=models.CharField(max_length=1000,null=True)
    Facility=models.CharField(max_length=1000,null=True)
    Ratings=models.FloatField(null=True)
    City=models.CharField(max_length=1000,null=True)
    Address=models.CharField(max_length=1000,null=True)
    Link=models.CharField(max_length=1000,null=True)
    
    def __str__(self):
        return self.name

