import requests

#Everyone has unique keys
key = "c15cdac2826b422a9d1550dc3b611f72"
api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + key
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append("Number " + str(i+1)+ ", " + json_data["articles"][i]["title"] + ".")

    return ar

