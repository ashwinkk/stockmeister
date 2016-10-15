from __future__ import absolute_import

from celery.task.schedules import crontab
from celery import shared_task
from .models import Symbols,Stocks_intraday
from .queries import query_curr
import requests,json

@shared_task
def update():
	ins = Symbols.objects.all()
	names = []
	if(len(ins)!=0):
		for symbol in ins:
			names.append(symbol.Symbol)
		query = query_curr(names)
		resp = requests.get(query)
		print resp.text
		add_to_stock(resp.text)

def add_to_stock(json_data):
	d = json.loads(json_data)
	d1 = d['query']
	d2 = d1['results']
	d3 = d2['quote']
	for stock in d3:
		instance = Stocks_intraday()
		instance.initialise(stock)
		instance.save()

def add_to_symbols(sym):
	for i in sym:
		instance = Symbols(Symbol=i)
		instance.save()

