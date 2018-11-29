n,k=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
if k in list:
    count=list.count(k)
    print ('yes')
else:
    print ('no')
