from django.shortcuts import render
from django.http import JsonResponse
from .models import Stocks_intraday
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def getdata(request):
	ins = Stocks_intraday.objects.all()
	data = {}
	array = []
	for each in ins:
		dic = each.parserform()
		array.append(dic)
	print array
	return JsonResponse({"results":array})