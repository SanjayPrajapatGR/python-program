number=int(input("enter the number"))
a=str(number)                        "convert number to string"
c=list(a)                            "split the digit from the string"
sum=0
for i in  range(1,len(a)+1,1):
    sum=sum +int(c[i-1])**i          
if(sum == number):
    print("true")
else:
    print("False")
