import requests
import json

#URL1 Current Conditions API
URL1 = 'http://dataservice.accuweather.com/currentconditions/v1/202200?apikey=rRkY3INvjmSTNITF5nZQLSmfJPb2Daki&language=id-ID&details=false&metric=true'
#URL2 1 Day of Daily Forecasts
URL2 = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/202200?apikey=rRkY3INvjmSTNITF5nZQLSmfJPb2Daki&language=id-ID&details=false&metric=true'

#request current condition URL1
r1 = requests.get(URL1).json()
r2 = requests.get(URL2).json()

#Currently
suhu1 = {'currently':[{'text': r1[0]['WeatherText'],'suhu': r1[0]['Temperature']['Metric']['Value']}]}
with open('suhu1.json', 'w') as osuhu1:
    json.dump(suhu1, osuhu1)
print("JSON suhu1 created")

#Daily
suhu2 = {'daily':[{'text':r2['Headline']['Text'],'min':r2['DailyForecasts'][0]['Temperature']['Minimum']['Value'],'max':r2['DailyForecasts'][0]['Temperature']['Maximum']['Value'],'day':r2['DailyForecasts'][0]['Day']['IconPhrase'],'night':r2['DailyForecasts'][0]['Night']['IconPhrase']}]}
with open('suhu2.json', 'w') as osuhu2:
    json.dump(suhu2, osuhu2)
print("JSON suhu2 created")
print("Everything must be OK now")
