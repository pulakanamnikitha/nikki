n=raw_input().rstrip()
digits=[]
for c in n:
    if c.isdigit():
        digits.append(c)
print ("".join(digits))
