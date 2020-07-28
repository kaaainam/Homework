import requests
# API 호출
response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

# reponse값을 json형식으로 불러오기
city_air = response_data.json()
#print(city_air['RealtimeCityAir']['row'][0]['NO2'])
a = city_air['RealtimeCityAir']['row']
for i in a:
    if i['PM10'] < 20:
        print(i['MSRSTE_NM'])
#    print(i['MSRSTE_NM'], i['PM10'])