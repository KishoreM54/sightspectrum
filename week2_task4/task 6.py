##x={"model":"tata",
##   "brand":"car"}
##y=x["model"]
##print(y)
##print(x.get("model"))
##---------find keys()----------
##x={"model":"tata",
##   "brand":"car"}
##y=x.keys()
##print(y)
##--------values----
##x={"model":"tata",
##   "brand":"car"}
##y=x.values()
##print(y)
##--------adding keys--------
##x={"model":"tata",
##   "brand":"car"}
##y=x.keys()
##print(y)
##x["car"]="old"
##print(y)
##---------add values------
##x={"model":"tata",
##   "brand":"car"}
##y=x.values()
##print(y)
##x["brand"]=2020
##print(y)
##
##x={"model":"tata",
##   "brand":"car"}
##print(x.items())
##----------add dict values-----
##x={"model":"tata",
##   "brand":"car"}
##y=x.items()
####print(y)
##x["tyre"]=2020
##print(y)
##---------------fromkeys--------------dict.fromkeys(var1,var2)
##x="dash","dash1",4
##y="join"
##a=dict.fromkeys(x,y)
##print(a)
##x="dash","dash1",4
##y="join"
##a=fromkeys(x,y)
##print(a)

##x={"model":"tata",
##   "brand":"car"}
##if "brand"in x:
##    print("yes sun is one of the key in x dictionary")

##-------change items---------x[keys]=new value
##x={"model":"tata",
##   "brand":"car",
##   "age":26}
##y=x["date"]=25
##print(type(y))
##print(x)
####--------update dict--->x.update({func})
##x={"model":"tata",
##   "brand":"car"}
##x.update({"brand":45})
##print(x)

##x={"model":"tata",
##   "brand":"car",
##   "no key found":"man"}
##y=x["name"]
##print(y)
##print(x.get("model","brand"))
##x={"model":"tata",
##   "brand":"car"}
##print(x["brand"])
##var = {"name":{1:{"surname":["s","m","n"]}}}
##var["name"][1]["surname"][2]="l"
##print(var)
##y=var.values({1:{"surname":["s","m","l"]}})
##print(y)

##var = {"name":[1:{"surname":["s","m","n"]}]}
##var = {"name":{1:{"surname":["s","m","n"]}}},"jega":{1:{"surname":["s","m","n"]}}#.........{{{[]}}}{{[]}}
##var = {"name":{1:{"surname":["s","m","n"]}},"jega":{1:{"surname":["s","m","n"]}}}
##var["jega"][1]["surname"][1]="l"
##print(var)

##var = '{"country":"india"}'
##dict[country[i]] = india[i]
##print(var)
##
##import json
##var = '{"country":"india"}'
##print(type(var))
##output = json.loads(var)
##print(type(output))
##print(output)

import json
x='{"sound ":"horn"}'
print(type(x))
output = json.loads(x)
print(type(output))
print(output)

















