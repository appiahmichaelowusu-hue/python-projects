import requests
import pandas as pd
url="https://restcountries.com/v3.1/all?fields=name,population,area,capital,region"
response=requests.get(url)
data=response.json()
df=pd.DataFrame(data)
df['country_name'] = df['name'].apply(lambda x: x['common'])

while True:
    print("1. Search for a specific country")
    print("2. View top 5 most populous countries ")
    print("3. View top 5 largest countries by area")
    print("4. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        country_name=input("Enter the name of the country: ")
        country_info=df[df['country_name'].str.lower()==country_name.lower()]
        if not country_info.empty:
            print(country_info[['country_name', 'population', 'area', 'capital', 'region']])
        else:
            print("Country not found.")
    elif choice=="2":
        top_populous=df.sort_values(by='population', ascending=False).head(5)
        print(top_populous[['country_name', 'population']])
    elif choice=="3":
        top_largest=df.sort_values(by='area', ascending=False).head(5)
        print(top_largest[['country_name', 'area']])
    elif choice=="4":
        break
    else:
        print("Invalid choice. Please try again.")

df.to_csv("countries.csv", index=False)