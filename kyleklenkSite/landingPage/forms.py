from django import forms

class BuyStockForm(forms.Form):
    stockTicker = forms.CharField(max_length=15)
    buyPrice = forms.FloatField()
    shares = forms.IntegerField()
