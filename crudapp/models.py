from django.db import models

# Create your models here.
class Crud(models.Model):
    slno=models.IntegerField
    itemname=models.CharField(max_length=250)
    desc=models.CharField(max_length=500)

    def __str__(self):
        return self.itemname
