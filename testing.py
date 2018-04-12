import urllib.request
import json

weather_token = ""
Data_set = ""
url = 'http://opendata.cwb.gov.tw/api/v1/rest/datastore/{Data_set}?sort=time'.format(Data_set=Data_set)
request = urllib.request.Request(url)

request.add_header( 'Authorization' , weather_token)
with urllib.request.urlopen(request) as response:
    f = open('temp.txt', 'w', encoding='utf-8')
    f.write(response.read().decode('utf-8'))
    #raw_data = json.loads(response.read().decode('utf-8'))
