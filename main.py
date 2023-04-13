import requests,time

def proccess_data(data):
    return {"city":data['name'],"datetime":time.ctime(int(data['dt'])),"type":data['weather'][0]['main'],"temp":data['main']['temp'],"humidity":data['main']['humidity']}
    


def get_weather_data(city='Tehran',appid='5a3f1f3994aea5d283d4cbc4204984b3'):
    URL = "https://api.openweathermap.org/data/2.5/weather"
    PARAMS = {'q' :city ,'appid' :appid } 
    r = requests.get(url = URL, params = PARAMS) 
    return proccess_data (r.json()) 

while True:
    print(get_weather_data("Malayer"))
    time.sleep(5)