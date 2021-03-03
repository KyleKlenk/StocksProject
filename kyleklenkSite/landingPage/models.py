from django.db import models

# Create your models here.
class Stocks(models.Model):
    tickerSymbol = models.CharField(max_length=15, primary_key=True)
    buyPrice = models.FloatField(default=0.0)
    currentPrice = models.FloatField(default=0.0)
    percentage = models.FloatField(default=0.0)
    shares = models.IntegerField(default=0)

class Transactions(models.Model):
    dateAndTime = models.DateTimeField(auto_now_add=True)
    stockTicker = models.CharField(max_length=15)
    price = models.FloatField(default=0.0)
    shares = models.IntegerField(default=0)
    transactionType = models.CharField(max_length=10)
    description = models.TextField()

