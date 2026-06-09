from bs4 import BeautifulSoup

html = open("index.html").read()
soup = BeautifulSoup(html, "html.parser")

# find by tag
h1 = soup.find("h1")
print(h1.text)  # Hello World

# find by class
intro = soup.find("h2", class_="intro")
print(intro.text)  # About me

# find by id
about = soup.find("p", id="about-me")
print(about.text)  # I am a web developer...

# find all list items
hobbies = soup.find_all("li")
for hobby in hobbies:
    print(hobby.text)