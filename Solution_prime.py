n1= int(input("Enter the lower limit: "))
n2= int(input("Enter the upper limit: "))
for val in range(n1,n2+1):
    if(val>1):
        for i in range(2,val):
            if(val%i==0):
                #print("Not prime")
                break
        else:
            print(val)
