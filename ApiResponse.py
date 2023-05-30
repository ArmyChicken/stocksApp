import requests, os
from dotenv import load_dotenv
 

class ApiFinance:
	def __init__(self):
		self.loadenv = load_dotenv()
		self.KEY = os.getenv('API_KEY')
		self.HOST = os.getenv('API_HOST')
		self.url = "https://yfinance-stock-market-data.p.rapidapi.com/stock-info"

		
		self.headers = {
			"content-type": "application/x-www-form-urlencoded",
			"X-RapidAPI-Key": self.KEY,
			"X-RapidAPI-Host": self.HOST
		}


	'''	def ticker():
			print('Enter your stock ticker')
			global stockInput 
			stockInput = input()'''
		

	def api(self,ticker):

		payload = { f"symbol": {ticker} }

		response = requests.post(self.url, data=payload, headers=self.headers)

		json = response.json()
		apiData = {
			'currency': json['data']['currency'],
			'stockPrice' : json['data']["currentPrice"],
			'exchange' : json['data']["exchange"],
			'companyName' : json['data']["longName"],
			'companySector' : json['data']['sector'],
			'stockSymbol' : json['data']['symbol'],
			'marketCap' : json['data']['marketCap']

		}
		# currency = json['data']['currency']
		# stockPrice = json['data']["currentPrice"]
		# exchange = json['data']["exchange"]
		# companyName = json['data']["longName"]
		# companySector = json['data']['sector']
		# stockSymbol = json['data']['symbol']
		# marketCap = json['data']['marketCap']
		return apiData
		#print(currency,stockPrice,exchange,companyName,companySector,stockSymbol)