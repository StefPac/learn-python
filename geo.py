import urllib.request, json
print("GEO")
ip = input("Enter an IP to locate: ")
url = "http://ip-api.com/json/" + ip
print(url)
res = urllib.request.urlopen(url)
data = json.load(res)
print("City:", data["city"])
print("Latitude:", data["lat"])
print("Longitude:", data["lon"])
