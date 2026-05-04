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
print(data)