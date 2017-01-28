numlist=[]
for i in range(1,10001):
    alist=[n for n in range(1,i-1) if i%n==0]
    if sum(alist)==i:
        numlist.append(i)
                
for i in numlist:
    blist=[n for n in range(1,i-1) if i%n==0]
    print ("divisor",blist, "for",i)