import requests

response = requests.get("http://colormind.io/api")
print(response.status_code)
response.json

print(dir(response))
print(response.content)
print(response.encoding)