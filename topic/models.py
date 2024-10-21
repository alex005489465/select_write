# models.py
from django.db import models

class SalesForm_Data(models.Model):
    productName = models.CharField(max_length=100)
    productFeatures = models.TextField()
    style = models.CharField(max_length=50)
    wordCount = models.IntegerField()
    otherRequirements = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.productName

