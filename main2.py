f = open("myText.txt", "r")
s=[]
for a in f:
    s.append(a)
s.sort()
print (s)
f.close()