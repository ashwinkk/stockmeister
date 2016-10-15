from django.db import models

# Create your models here.
class Stocks_intraday(models.Model):
	_id = models.AutoField(primary_key=True)
	Symbol = models.CharField(max_length=20,blank=True)
	Name = models.CharField(max_length=20,blank=True,null=True)
	LastTradePriceOnly = models.CharField(max_length=20,blank=True,null=True)
	Change = models.CharField(max_length=20,null=True)
	ChangeinPercent = models.CharField(max_length=20,blank=True,null=True)

	def initialise(self,stock_data):
		f = open('fields.txt','r')
		w = f.read()
		attrs = w.split(' ')
		print attrs
		i=0
		while i<(len(attrs)):
		 	setattr(self,attrs[i],stock_data[attrs[i]])
		 	i = i + 1
		f.close()

	def parserform(self):
		import os
		f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'fields.txt'),'r')
		w = f.read()
		attrs = w.split(' ')
		i=0
		dic = {}
		while i<(len(attrs)):
			dic[attrs[i]] = getattr(self,attrs[i])
			i=i+1
		f.close()
		return dic


class Stocks_interday(models.Model):
	Symbol = models.CharField(max_length=20,blank=True,primary_key=True)
	Volume = models.CharField(max_length=20,blank=True,null=True)
	Open = models.CharField(max_length=20,blank=True,null=True)
	Close = models.CharField(max_length=20,blank=True,null=True)
	High = models.CharField(max_length=20,blank=True,null=True)
	Low = models.CharField(max_length=20,blank=True,null=True)
	Adj_Close = models.CharField(max_length=20,blank=True,null=True)
	Date = models.CharField(max_length=20)

	def initialise(self,stock_data):
		self.Symbol = stock_data['Symbol']
		self.Volume = stock_data['Volume']
		self.Open = stock_data['Open']
		self.Close = stock_data['Close']
		self.High = stock_data['High']
		self.Low = stock_data['Low']
		self.Adj_Close = stock_data['Adj_Close']
		self.Date = stock_data['Adj_Close']

class Symbols(models.Model):
	Symbol = models.CharField(max_length=20,primary_key=True)