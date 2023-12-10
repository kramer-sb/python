import requests

city = 'London' #can put in any city 
url = 'http://api.weatherapi.com/v1/current.json?key=2e2aab2c96184e6db1b161421231012&q='+city+' &aqi=no' #this is grabbing weaterh from weather api
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_f')
description = weather_json.get('current').get('condition').get('text')

print("Today's weather in",  city,  "is", description, 'and',  temp, 'degrees')

#this will print: Today's weather in London is Partly cloudy and 53.6 degrees (at the time this was run initially).
