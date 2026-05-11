import pandas as pd

data={
    "Name": ["Kumasi Orhanage", "Accra Orhanage", "Tamale Orhanage" , "Bolgatanga Orhanage", "Sunyani Orhanage"],
    "Age": [12, 25, 34, 45, 56],
    "Location": ["Kumasi", "Accra", "Tamale", "Bolgatanga", "Sunyani"],
    "Meals Received": [3, 2, 4, 5, 6]

}
df=pd.DataFrame(data)
print(df)
print(df["Age"].mean())
print(df[df["Age"] > 18])
df.to_csv("beneficiaries.csv", index=False)

df2=pd.read_csv("beneficiaries.csv")
print(df2)