# parsed_data/models.py
from django.db import models

# CU Product
class Product(models.Model):
    prodId = models.AutoField(primary_key=True)
    prodName = models.CharField(max_length=255, unique=True, null=False)
    prodType = models.CharField(max_length=20)
    prodEventType = models.CharField(max_length=20, default="DEFAULT")
    prodPrice = models.PositiveIntegerField(null=False)
    prodImg = models.URLField(null=True)

    class Meta:
        ordering = ['prodName']

    def __str__(self):
        return self.prodName


# Emart24 Product
class Product2(models.Model):
    prodId = models.AutoField(primary_key=True)
    prodName = models.CharField(max_length=255, unique=True, null=False)
    prodType = models.CharField(max_length=20)
    prodEventType = models.CharField(max_length=20, default="DEFAULT")
    prodPrice = models.PositiveIntegerField(null=False)
    prodImg = models.URLField(null=True)

    class Meta:
        ordering = ['prodName']

    def __str__(self):
        return self.prodName


# GS25 Product
class Product3(models.Model):
    prodId = models.AutoField(primary_key=True)
    prodName = models.CharField(max_length=255, unique=True, null=False)
    prodType = models.CharField(max_length=20)
    prodEventType = models.CharField(max_length=20, default="DEFAULT")
    prodPrice = models.PositiveIntegerField(null=False)
    prodImg = models.URLField(null=True)

    class Meta:
        ordering = ['prodName']

    def __str__(self):
        return self.prodName


# SevenEleven Product
class Product4(models.Model):
    prodId = models.AutoField(primary_key=True)
    prodName = models.CharField(max_length=255, unique=True, null=False)
    prodType = models.CharField(max_length=20)
    prodEventType = models.CharField(max_length=20, default="DEFAULT")
    prodPrice = models.PositiveIntegerField(null=False)
    prodImg = models.URLField(null=True)

    class Meta:
        ordering = ['prodName']

    def __str__(self):
        return self.prodName


# MiniStop Product
class Product5(models.Model):
    prodId = models.AutoField(primary_key=True)
    prodName = models.CharField(max_length=255, unique=True, null=False)
    prodType = models.CharField(max_length=20)
    prodEventType = models.CharField(max_length=20, default="DEFAULT")
    prodPrice = models.PositiveIntegerField(null=False)
    prodImg = models.URLField(null=True)

    class Meta:
        ordering = ['prodName']

    def __str__(self):
        return self.prodName


class Post(models.Model):
    user_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
