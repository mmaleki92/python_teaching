import urllib.request

url = "https://www.example.com/"
response = urllib.request.urlopen(url)

with response as f:
    contents = f.read().decode("utf-8")
    print(contents)