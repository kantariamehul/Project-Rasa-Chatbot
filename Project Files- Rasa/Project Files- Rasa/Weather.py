# importing requests and json
import requests

def Weather_fun():
    # base URL
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Rajkot"
    API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

    # upadting the URL
    #URL = https://api.openweathermap.org/data/2.5/weather?q=Rajkot&appid=f6ca853d9492e9ef96edce9c188fc090
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request

    if response.status_code == 200:
       # getting data in the json format
       data = response.json()

       # getting the main dict block
       main = data['main']
       weather=data["weather"][0]
       clouds=weather['description']
       temperature = int(main['temp']-273.15)
       humidity=main['humidity']
       #print(main)
       #print(weather)
       #print(clouds)
       #print(temperature)
       #print(humidity)
       Rajkot_weather="clouds:"+clouds+",\ntemperature:"+str(temperature)+" C,\nhumidity:"+str(humidity)+"%"
       print(Rajkot_weather)
    else:
       # showing the error message
       print("Error in the HTTP request")
       #temperature=0
       Rajkot_weather="NULL"

    #return temperature
    return Rajkot_weather

#Weather_fun()
