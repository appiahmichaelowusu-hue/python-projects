import sys

if len(sys.argv) < 3:  # less than 3 items = missing arguments
    print("Usage: python hello.py [name] [country]")
else:
    name = sys.argv[1]      # second item = name
    country = sys.argv[2]   # third item = country
    print(f"Hello {name}, you are from {country}")