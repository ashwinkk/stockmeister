from django.shortcuts import render
from newprofuser.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def Login(request):
	userdata = request.POST
	username = userdata.get('uname')
	password = userdata.get('password')
	res = User.objects.filter(uname=username,password=password)
	if len(res)!=0:
		user = res[0]
		dic = {'portfolio':user.portfolios,'name':user.name,'status':True}
	else:
		dic = {'status':False}
	return JsonResponse(dic)