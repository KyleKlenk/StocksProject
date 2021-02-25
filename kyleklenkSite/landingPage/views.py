from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import BuyStock
# Create your views here.

@login_required(login_url="/login")
def landingPage(request):
    #getStocksDataBase()
    return render(request, "landingPage/landingPage.html")

def getStocksDataBase():
    stocks = BuyStock.objects.all()
    for stock in stocks:
        print(stock.tickerSymbol)
        print(stock.buyPrice)

def loginPage(request):
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

def logoutPage(request):
    if request.method == 'POST':
        logout(request)
        return redirect("/login")





