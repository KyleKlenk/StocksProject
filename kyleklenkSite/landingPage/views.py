from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import BuyStock
from django.core import serializers
from .stockTicker import StockTicker
from .forms import BuyStockForm
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
# Create your views here.

@login_required(login_url="/login")
def landingPage(request):
    #getStocksDataBase()

    return render(request, "landingPage/landingPage.html")

async def getStocks(request):
    todaysDate = dt.datetime(dt.date.today().year, 
                dt.date.today().month, 
                dt.date.today().day)

    stocks = BuyStock.objects.all()
    for stock in stocks:
        df = web.DataReader(stock.tickerSymbol, 'yahoo', todaysDate, todaysDate)
        stock.currentPrice = round(df.iloc[0]["Close"], 2)
        stock.percentage = round(
            ((stock.currentPrice - stock.buyPrice) / stock.buyPrice) * 100, 2
        )
        stock.save()
    
    stocksJson = serializers.serialize('json', stocks)
    return HttpResponse(stocksJson, content_type='application/json')

async def buyStock(request):
    print(request.POST.get('stockTicker'))
    print(request.POST.get('buyPrice'))
    print(request.POST.get('shares'))
    return HttpResponse()

async def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'landingPage/loginPage.html', {'form':form})

async def logoutPage(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/login")





