from os import *
from platform import *
def ଓଜନ(a):
    return path.getsize(a)#file size in byte
    
def କଣଅଛି(a):
    return listdir(a)

def ଜାଣିନି(a):
    return help(a)
କେଉଁଜାଗା=getcwd()#current directory o
ସଞ୍ଚାଳକ=processor()#computer processor name p
ସଞ୍ଚାଳକସଂସ୍କରଣ=architecture()#computer bit 32/64 p
ସଞ୍ଚାଳକନାମ=machine()#amd64 p
କମ୍ପ୍ୟୁଟରନାମ=node()#computer name p
ପରିଚାଳନାନାମସଂସ୍କରଣ=platform()#osname p
ପରିଚାଳନାନାମ=system()#which os p


print(ଜାଣିନି('modules'))
print(ଓଜନ("allalgo.py"))
print(କେଉଁଜାଗା)
print(ସଞ୍ଚାଳକ)
print(ସଞ୍ଚାଳକସଂସ୍କରଣ)
print(ସଞ୍ଚାଳକନାମ)
print(କମ୍ପ୍ୟୁଟରନାମ)
print(ପରିଚାଳନାନାମସଂସ୍କରଣ)
print(ପରିଚାଳନାନାମ)
print(କଣଅଛି("/"))
ଦେଖ=print
ଦେଖ("ଆଜି ଆମେ")