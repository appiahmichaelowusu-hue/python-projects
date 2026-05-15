import requests

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=jack+johnson")
data=response.json()
print(data["results"][0]["trackName"])
print(data["results"][0]["artistName"])
print(data["results"][0]["trackNumber"])
