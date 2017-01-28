numset=(range(1,20001))
numlist=[i for i in numset if i%5!=0 and i%3==0]
#print ("list of numbers: ",numlist)    
print ("first 10 numbers: ", numlist[0:10])
print ("last 5 numbers: ", numlist[len(numlist)-5:len(numlist)])
print ("even  in list: ", numlist[::2])
#print ("cutlist： ",numlist[0:10]+numlist[len(numlist)-5:len(numlist)]+numlist[::2])
print ("reverse numlist",numlist[len(numlist):0:-1])