from django.shortcuts import render
from django.http import HttpResponse
from .models import BuyStock
# Create your views here.

def landingPage(request):
    getStocksDataBase()
    return render(request, "landingPage/landingPage.html")

def getStocksDataBase():
    stocks = BuyStock.objects.all()
    for stock in stocks:
        print(stock.tickerSymbol)
        print(stock.buyPrice)


