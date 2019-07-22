import requests
import os

snooth_key = os.getenv("SNOOTH_KEY")
ip_add = os.getenv("IP")

address = "http://api.snooth.com/wines/"
key = "?akey=" + snooth_key 
ip = "&ip=" + ip_add
t = "&t=wine"   #return only wine
n = "&n=3"      #number of results to return
mr = "&mr=3"
lang = "&lang=en"

req_string = address + key + ip + t + n + mr + lang 


print(req_string)

#req = requests.get(req_string)
#print(req.text)

#open and save to file
#result = open("req_result.txt", "w")
#result.write(req.text)
#result.close


