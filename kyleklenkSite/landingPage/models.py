from django.db import models

# Create your models here.
class BuyStock(models.Model):
    tickerSymbol = models.CharField(max_length=15)
    buyPrice = models.FloatField(default=0.0)