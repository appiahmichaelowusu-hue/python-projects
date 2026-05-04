import requests
amount=int(input("Enter the amount of Ghana Cedis you want to convert: "))
url="https://api.exchangerate-api.com/v4/latest/GHS"

response=requests.get(url)
data=response.json()
print(data)