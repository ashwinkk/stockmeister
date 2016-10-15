import requests,json

url="http://localhost:8000/test/"
header={'content-type':'application/json'}
data={'stocks':['AAPL','GOOG','YHOO','MSFT']}
resp = requests.post(url,data=json.dumps(data),headers=header)
print resp.text
