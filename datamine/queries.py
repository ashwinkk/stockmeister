from datetime import date,timedelta

def query_curr(params):
	head='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22'
	body=''
	for symbol in params:
		body = body + symbol +'%22%2C%22' 
	#YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22
	foot=')&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
	query = head + body[0:len(body)-6] + foot
	return query

def query_hist(params):
	head = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.historicaldata%20where%20symbol%20in(%20%22'
	symbols=''
	for symbol in params:
		symbols = symbols + symbol +'%22%2C%22' 
	now = date.today()
	week = timedelta(days=7)
	past = now-week
	duration = ')%20and%20startDate%20%3D%20%22'+past.isoformat()+'%22%20and%20endDate%20%3D%20%22'+now.isoformat()
	foot = '%22&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback='
	query = head + symbols[0:len(symbols)-6]+duration+foot
	return query