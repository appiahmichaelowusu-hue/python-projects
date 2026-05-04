import requests


amount=int(input("Enter the amount of Ghana Cedis you want to convert: "))
url="https://api.exchangerate-api.com/v4/latest/GHS"

response=requests.get(url)
data=response.json()

exchange_rate_USD=data["rates"]["USD"]
exchange_rate_EUR=data["rates"]["EUR"]
exchange_rate_GBP=data["rates"]["GBP"]
amount_in_USD=amount*exchange_rate_USD
amount_in_EUR=amount*exchange_rate_EUR
amount_in_GBP=amount*exchange_rate_GBP

print(f"Convertion rate of Ghana Cedis to US Dollars: {exchange_rate_USD}")
print(f"Convertion rate of Ghana Cedis to Euros: {exchange_rate_EUR}")
print(f"Convertion rate of Ghana Cedis to British Pounds: {exchange_rate_GBP}")
print(f"{amount} Ghana Cedis is equal to {amount_in_USD:.2f} US Dollars")
print(f"{amount} Ghana Cedis is equal to {amount_in_EUR:.2f} Euros")
print(f"{amount} Ghana Cedis is equal to {amount_in_GBP:.2f} British Pounds")