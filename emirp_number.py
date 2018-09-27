number=int(input("enter the number"))
count=0
for i in range(1,number+1,1):
    if(number%i == 0):                    " check prime or not
        count=count+1
if(count == 2):
    count1=0
    y=str(number)                         "convert number into string
    z=y[::-1]                             " revese the string
    z=int(z)                              " convert  reverse string into intger
    for i in range(1,z+1,1):
        if(z%i == 0):                     " check reverse number for prime
            count1=count1+1
    if(count1 == 2):
        print("the number is emirp")
    else:
        print("the number is not emirp")
else:
    print("the number is not emirp")
