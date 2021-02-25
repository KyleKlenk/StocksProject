from django.db import models

# Create your models here.
class BuyStock(models.Model):
    tickerSymbol = models.CharField(max_length=15, primary_key=True)
    buyPrice = models.FloatField(default=0.0)
    currentPrice = models.FloatField(default=0.0)
    percentage = models.FloatField(default=0.0)
    shares = models.IntegerField(default=0)

class transaction(models.Model):
    dateAndTime = models.DateTimeField(auto_now_add=True)
    stockTicker = models.CharField(max_length=15)
    buyPrice = models.FloatField(default=0.0)
    shares = models.IntegerField(default=0)
    description = models.TextField()

