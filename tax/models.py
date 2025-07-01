from django.db import models

# Create your models here.

class ActualAmount(models.Model):
    totalamount=models.FloatField()
    tax=models.FloatField(default=1.106470588)
    actualamount=models.FloatField()
    
class TotalAcutalamount(models.Model):
    totalacutalamount=models.FloatField()