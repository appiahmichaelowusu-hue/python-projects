import requests

while True:
    try:
     city=input("Enter a city :")
     break
    except  :
        print("Invalid input. Please enter a valid city name.")
       
url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)
data = response.json()

temp = data['current_condition'][0]['temp_C']
description = data['current_condition'][0]['weatherDesc'][0]['value']
humidity = data['current_condition'][0]['humidity']
visibility= data['current_condition'][0]['visibility']

print(f"City: {city}")
print(f"Temperature: {temp}°C")
print(f"Weather: {description}")
print(f"Humidity: {humidity}%")
print(f"Visibility: {visibility} km")