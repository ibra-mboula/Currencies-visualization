import requests

url = 'https://api.exchangerate.host/timeseries?start_date=2020-01-01&end_date=2020-01-04'
response = requests.get(url)
data = response.json()

print(data)
        