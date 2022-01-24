import requests
#a=input("city name")
key= "4fb9e03396690b77da72f9a65891b60d"
api_address=f'hhttp://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID' +key
json_data=requests.get(api_address).json()

def temp():
    temperature=round(json_data["main"]["temp"-273,1])
    return temperature

def des():
    description=json_data["weather"][0]["description"]
    return description

print(temp())
print(des())
