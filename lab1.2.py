x=int(input("enter an integer:"))
y=float(input("enter an fload number:"))
z=input("enter another number:")
    
def main(x,y,z):
    if x>y and x>z:
        print ("bigest number: ",x)
    elif y>x and y>z:
        print ("bigest: ", y)
    elif z>x and z>y:
        print ("bigest: ",z)
    else:
        print ("please define comparible numbers again")
        
main(x,y,z)