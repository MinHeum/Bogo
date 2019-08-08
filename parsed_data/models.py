# parsed_data/models.py
from django.db import models


class Product(models.Model):
    prodId = models.AutoField(primary_key=True)
    prodName = models.CharField(max_length=255, unique=True, null=False)
    prodType = models.CharField(max_length=20)
    prodEventType = models.CharField(max_length=20)
    prodPrice = models.PositiveIntegerField(null=False)
    prodPriceEach = models.PositiveIntegerField
    # prodCVS = models.CharField(max_length=40, null=False)
    prodImg = models.URLField(null=True)

    class Meta:
        ordering = ['prodName']

    def calculate_each_price(self):
        if self.prodEventType is '1+1':
            self.prodPriceEach = int(self.prodPrice / 2)
        elif self.prodEventType is '2+1':
            self.prodPriceEach = int(self.prodPrice / 3)
        elif self.prodEventType is '3+1':
            self.prodPriceEach = int(self.prodPrice / 4)
        elif self.prodEventType is '4+1':
            self.prodPriceEach = int(self.prodPrice / 5)
        else:
            print("[ERROR] CANNOT FOUND Wrong ProdEventType!!!")

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
