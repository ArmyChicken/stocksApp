import requests, os
from dotenv import load_dotenv
 

class ApiFinance:
	def __init__(self):
		self.loadenv = load_dotenv()
		self.KEY = os.getenv('API_KEY')
		self.HOST = os.getenv('API_HOST')



	'''	def ticker():
			print('Enter your stock ticker')
			global stockInput 
			stockInput = input()'''
		

	def api(self,ticker):
		
		
		url = f"https://yahoo-finance127.p.rapidapi.com/price/{ticker}"

		headers = {
			"X-RapidAPI-Key": self.KEY,
			"X-RapidAPI-Host": self.HOST
		}

		response = requests.get(url, headers=headers)

		print(response.json())