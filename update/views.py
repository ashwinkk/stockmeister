from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from newprofuser.models import User

# Create your views here.
@csrf_exempt
def update(request):
	userdata = request.POST
	username = userdata.get('uname')
	password = userdata.get('password')
	res = User.objects.filter(uname=username,password=password)
	if len(res)!=0:
		user = res[0]
		portfolios = json.loads(userdata.get('portfolios'))
		user.portfolios = portfolios
		user.save()
		dic={'status':True}
	else:
		dic={'status':False}
	return JsonResponse(dic)