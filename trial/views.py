from django.shortcuts import render
from django.contrib.staticfiles.views import serve
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json,requests
from .models import User,Stocks,Symbols
from django.views.decorators.csrf import csrf_exempt
from .querybuilder import querybuild

# Create your views here.
@csrf_exempt
def test(request):
	#stock = json.loads(request.body)
	#query1 = querybuild(['AAPL','GOOG','YHOO','MSFT'])
	#data = requests.get(query1)
	#add_to_stock(data.text)
	#add_to_symbols(stock['stocks'])
	#dic = {"response":data.text}
	return serve(request,"abc.zip")

def add_to_stock(json_data):
	d = json.loads(json_data)
	d1 = d['query']
	d2 = d1['results']
	d3 = d2['quote']
	for symbols in d3:
		instance = Stocks(Ask=symbols['Ask'],PreviousClose=symbols['PreviousClose'],Open=symbols['Open'],Symbol=symbols['Symbol'])
		instance.save()

def add_to_symbols(sym):
	for i in sym:
		instance = Symbols(Symbol=i)
		instance.save()
