from django.db import models

# Create your models here.


class Product(models.Model):
    prodId = models.AutoField(primary_key=True)
    prodName = models.CharField("상품이름", max_length=255, unique=True, null=False)
    prodType = models.CharField("분류", max_length=20)
    prodEventType = models.CharField("n+1", max_length=20)
    prodPrice = models.PositiveIntegerField(null=False)
    prodPriceEach = models.PositiveIntegerField

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
        else :
            print("[ERROR] CANNOT FOUND Wrong ProdEventType!!!")

    def __str__(self):
        return self.prodName


class Image(models.Model):
    ImgId = models.AutoField(primary_key=True)
    ImgURL = models.URLField(null=True)
    prodId = models.ForeignKey(
        'Product.prodId',
        on_delete=models.SET_NULL(),
        related_name='prod',
        related_query_name='prodId'
    )

    def __str__(self):
        return self.ImgURL
