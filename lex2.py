c=(raw_input().split())
c.sort()
l=[]
s=[]
for i in c:
    l.append(len(i))
l.sort()
for x in l:
    for y in c:
        if(len(y)==x):
            if y not in s:
                s.append(y)
print(" ".join(s))
