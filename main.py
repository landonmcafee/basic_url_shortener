import pyshorteners

url = input("Please enter a URL: ")
shortener = pyshorteners.Shortener()
shortened_url = shortener.tinyurl.short(url)

print(shortened_url)
