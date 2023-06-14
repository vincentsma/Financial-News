import requests
import json

def get_latest_price(symbol):
    try:
        api_key = ""
        base_url = "https://www.alphavantage.co/query?"
        function = "GLOBAL_QUOTE"

        # define the payload
        payload = {
            "function": function,
            "symbol": symbol,
            "apikey": api_key
        }

        # make the request
        response = requests.get(base_url, params=payload)

        # parse the response
        data = json.loads(response.text)

        # get the latest price
        latest_price = float(data["Global Quote"]["05. price"])

        return latest_price
    except:
        return 0
# list of companies
companies = ["AAPL", "MSFT", "GOOG", "AMZN", "FB", "TSLA", "BRK.B", "V", "JNJ", "WMT"]




class IEXCloudAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://cloud.iexapis.com/stable'

    def get_top_10_companies(self):
        endpoint = f'{self.base_url}/stock/market/list/mostactive'

        params = {
            'token': self.api_key,
        }

        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            company_data = response.json()[:10]
            return company_data
        else:
            print(f'Error: {response.status_code}')

api_key = ''




class PolygonAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.polygon.io/v2/aggs/ticker/'

    def get_stock_price(self, symbol):
        endpoint = f'{self.base_url}{symbol}/range/1/day/2023-01-09/2023-01-09'

        params = {
            'apiKey': self.api_key
        }

        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            stock_data = response.json()
            return stock_data['results'][0]['c']
        else:
            print(f'Error: {response.status_code}')


api_key = ''
polygon_api = PolygonAPI(api_key)
company_names = []
stock_prices = []

for company in companies:
    try:
        stock_price = polygon_api.get_stock_price(company)
        if stock_price is not None:
            company_names.append(company)
            stock_prices.append(stock_price)
    except Exception as e:
        print(f'Error fetching data for {company}: {e}')
        continue

print("Company Names:")
print(company_names)
print("-------------------------------------")
print("Stock Prices:")
print(stock_prices)

findata= "Do not return as an AI language model " + 'company_names'+str(company_names)+'\n stock prices'+str(stock_prices)




class OpenAIAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_base_url = 'https://api.openai.com/v1'

    def summarize_data(self, data):
        endpoint = "https://api.openai.com/v1/chat/completions"
        
        
    
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

        payload = {
            'model': "gpt-3.5-turbo",
            'messages': [{"role": "user", "content": data}],
            'frequency_penalty': 1,
            'presence_penalty': 1,
            'max_tokens': 100,
            'temperature': 0.3,
            'top_p': 1.0,
            'n': 1,
            'stop': None,
        }

        response = requests.post(endpoint, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content'].strip()
        else:
            print(f'Error: {response.status_code}')


api_key = ''
openai_api = OpenAIAPI(api_key)


summary = openai_api.summarize_data(findata)
print(f"Summary: {summary}")


with open('summary.txt', 'w') as file:
    file.write(summary)