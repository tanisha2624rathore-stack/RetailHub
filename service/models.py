from django.db import models

class Purchase_detail(models.Model):
    id=models.AutoField(primary_key=True)
    company_name=models.CharField(max_length=30)
    product_name=models.CharField(max_length=30)
    qty=models.IntegerField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    total_price=models.DecimalField(max_digits=6, decimal_places=2)
    delete=models.CharField(default="N",max_length=10)

# Create your models here.
