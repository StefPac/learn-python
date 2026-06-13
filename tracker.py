import urllib.request, json
print("TRACKER")
ip = input("Enter an IP to locate: ")
url = "http://ip-api.com/json/" + ip
res = urllib.request.urlopen(url)
data = json.load(res)
print("Provider:", data["isp"])
print("Owner:", data["org"])