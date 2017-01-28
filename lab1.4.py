import math

a=float(input ("bank fix interest: "))

def bank(a):
    if a>0:
        yearD=math.log(2,1+a)
        print ("it takes ",yearD,"years to double the money!")
    else:
        print("please enter a valid fix interest")

bank(a)