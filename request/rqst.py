import requests

r = requests.get('https://www.google.com/', stream=True)
# x = r.status_code

print(r.headers['Content-Encoding'])
print(r)
