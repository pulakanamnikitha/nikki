a=int(raw_input())
tot=0
while(a>0):
    dig=a%10
    tot=tot+dig
    a=a//10
print(tot)
