##to find a pattern in string and paragraphs

import re
text="welcome world"
x=re.compile("welcome world")
y=x.search(text)
print(y)

import re
text="1Welcome 1World"
x=re.compile("[a-zA-Z0-1]+")
y=x.search(text)
print(y)

##find al the patterns
##
import re
text="1Welcome 1world"
x=re.compile("[A-Z0-1]+")
y=x.findall(text)
print(y)

import re
text="contact me in kishorem@sightspectrum.in"
x= re.compile("[a-zA-Z]+@+[a-zA-Z]+\.[a-zA-Z0-9]+")
y=x.findall(text)
print(y)



import re
text="my name is gayu my contact mail id is gayathri@sightspectrum.in"
x=re.compile("[a-zA-Z0-1]+@+[a-zA-Z0-1]+\.[a-z]+")
y=x.findall(text)
print(y)


import re
text="gayu friend"
x=re.search(r"friend",text)
print(x)

import re
var=re.split(r"q","king queen")
print(var)

import re
var = re.split("q", "king queen")
print(var)
    






































