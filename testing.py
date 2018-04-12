import urllib.request
import json

weather_token = "CWB-605E85E4-5367-4916-A5E3-891848C1EC18"
Data_set = "F-C0032-001"
url = 'http://opendata.cwb.gov.tw/api/v1/rest/datastore/{Data_set}?sort=time'.format(Data_set=Data_set)
request = urllib.request.Request(url)

request.add_header( 'Authorization' , weather_token)
with urllib.request.urlopen(request) as response:
    f = open('temp.txt', 'w', encoding='utf-8')
    f.write(response.read().decode('utf-8'))
    #raw_data = json.loads(response.read().decode('utf-8'))
