# models.py
"""
from django.db import models

class SalesForm_Data(models.Model):
    productName = models.CharField(max_length=100)
    productFeatures = models.TextField()
    style = models.CharField(max_length=50)
    wordCount = models.IntegerField()
    otherRequirements = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.productName
"""
from django.db import models
from django.conf import settings

class SalesForm_Data(models.Model):
    sales_form_id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    productFeatures = models.TextField()
    style = models.CharField(max_length=50)
    wordCount = models.IntegerField()
    otherRequirements = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.productName

class Product_Artical(models.Model):
    product_artical_id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    productFeatures = models.TextField()
    style = models.CharField(max_length=50)
    wordCount = models.IntegerField()
    otherRequirements = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.productName
