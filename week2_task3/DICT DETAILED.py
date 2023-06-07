----------dictionary--------
x={"fish":"chick","dust":"bin"}
print(x)

---------list,tuple,=dict----------
x=["name","age"]
y=["kishore","shalu"]
z=dict(zip(x,y))
print(z)
x=["name","age"]
y=("kishore","shalu")
z=dict(zip(x,y))
print(z)
a={"mahi","virat"}
print(a)
b={"keeper","batsman"}

c=dict(zip(a,b))
print(c)
a={"mahi","virat","arjith"}
b={2,3,566}
c=dict(zip(a,b))
print(c)
------len-----------
a={"mahi":1,"virat":"bat"}
print(len(a))
a={"mahi","virat"}
---------membership operator-----
a={"mahi":"virat","aswin":23}
print("aswin"in a)
print(a)
a=["mahi","virat","aswin"]
print(a[1])

a={"mahi":"virat","aswin":32}
print(a["mahi"])
-----nested dict-------

nested={"arun":["argue","dance"],
 "language":{"speak":"english","age":23} }
print(nested["language"]["age"])
n={"arun":["argue","dance"],
 "language":{"speak":"english","age":23} }
print(n["arun"])
-------------print(n[key])-----------

---------modifying dict elements--------

a={"dance":"party",
   "tea":"time"}
a["dance"]="song"
print(a)
-------adding new dict values----
a={"dance":"party","tea":"time"}
a["dog"]="bark"
print(a)



x="how", "are","you"
x.remove("how")
print(x)
x.reverse()
print(x)
x=('how are you')
print(x[::-1])
print(x[:3:-1])
print(type(x))


a1="hello"
a2="there"
print("hello:",a1)
print("there:",a2)
a=a1+a2
print(a)
x={"name":"ajai",
   "age":25}
print(x)

n={["arun"]:"dance","language":{"speak":"english","age":23}}
print(n)
n={"arun":["argue","dance"],"language":{"speak":"english","age":23} }
print(n)




var = {"name":{"surname":["jhacfj",66,45]}}
var1=print(var["name"])
print(type(var1))

nested={"arun":"language","speak":"english","age":23} 
print(nested["arun"]["speak"]["age"])
