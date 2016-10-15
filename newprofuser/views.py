from .models import User
from django.http import JsonResponse
from datamine.models import Symbols
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def newuser(request):
	userdata = request.POST
	username = userdata.get('uname')
	password = userdata.get('password')
	res = User.objects.filter(uname=username)
	if len(res)==0:
		name = userdata.get('name')
		email = userdata.get('emid')
		portfolios = json.loads(userdata.get('portfolios'))
		portfolionames = portfolios.keys()
		for each in portfolionames:
			ins = Symbols(Symbol=portfolios[each]['symbol'])
			ins.save()
		user = User(uname=username,password=password,portfolios=portfolios,name=name,emailid=email)
		user.save()
		dic = {'status':True}
	else:
		dic = {'status':False}
	return JsonResponse(dic)