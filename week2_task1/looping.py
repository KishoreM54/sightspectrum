##---------------------------set methods-------------
##--------union()----------



##----------------intersection ------------
##r={"grape","set","dog","man"}
##s={"man","women","set"}
##print(r.intersection(s))
####----------intersection_update-----------
##r={"grape","dora","set","dog","man"}
##s={"man","women","set"}
##r.intersection_u
##pdate(s)
##print(r)
##--------diference------------
##s={"man","women","set"}
##t={"come","man","daisy"}
##print(s.difference(t))
##print(t.difference())

##------------difference_update-----------
##s={"man","women","set"}
##a={"come","man","daisy"}
##s.difference_update(a)
##print(s)
##a.difference_update(s)
##print(a)

##------------symmetric difference-----------
##s={"man","women","set"}
##a={"dog","man","set"}
##print(a.symmetric_difference(s))
##-----------------symmetric difference_update----------
##a={"ranveer","dhoni"}
##b={"sad","happy","dhoni"}
##b.symmetric_difference_update(a)
##print(b)

##--------------issubset--------------------
##a={"ranveer","dhoni"}
##b={"sad","happy","dhoni"}
##print(a.issubset(b))
##a={"ranveer","dhoni"}
##b={"sad","happy","dhoni","ranveer"}
##print(b.issubset(a))
##-------superset------------
##a={"ranveer","dhoni"}
##b={"sad","happy","dhoni"}
##print(b.issuperset(a))
##a={"ranveer","dhoni","sad","happy"}
##b={"sad","happy","dhoni"}
##print(a.issuperset(b))

##------------isdisjoint--------------
a={"ranveer","dhoni"}
b={"sad","happy","dhoni"}
print(a.isdisjoint(b))
a={"ranveer","sewag"}
b={"sad","happy","dhoni"}
print(a.isdisjoint(b))





##
##
##
##a=[1,3,"ranveer"]
##b=["sad","happy"]
##a.extend(b)
##print(a)
##
##a={1,3,"ranveer"}
##b={"sad","happy"}
##a.extend(b)
##print(a)
