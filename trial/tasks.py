from __future__ import absolute_import

from celery.task.schedules import crontab
from celery import shared_task
from .models import Symbols,Stocks
from .querybuilder import querybuild
import requests,json

@shared_task
def update():
	ins = Symbols.objects.all()
	names = []
	for symbol in ins:
		names.append(symbol.Symbol)
	query = querybuild(names)
	resp = requests.get(query)
	print resp.text
	add_to_stock(resp.text)

def add_to_stock(json_data):
	d = json.loads(json_data)
	d1 = d['query']
	d2 = d1['results']
	d3 = d2['quote']
	for stock in d3:
		instance = Stocks()
		instance.initialise(stock)
		instance.save()

def add_to_symbols(sym):
	for i in sym:
		instance = Symbols(Symbol=i)
		instance.save()