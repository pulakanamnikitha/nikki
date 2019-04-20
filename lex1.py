b=(raw_input().split())
b.sort()
l=[]
s=[]
for i in b:
    l.append(len(i))
l.sort()
for x in l:
    for y in b:
        if(len(y)==x):
            if y not in s:
                s.append(y)
print(" ".join(s))
