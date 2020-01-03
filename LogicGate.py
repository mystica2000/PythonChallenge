print("\n enter the Logic gate")
res=input()
a=int(input("enter First input"))
b=int(input("enter Second input"))
if(res=='OR'):
    print("Result =",a or b)
elif(res=='AND'):
    print("Result =",a and b)
elif(res=='XOR'):
    print("Result =",a ^ b)
elif(res=='NAND'):
    print("Result =",int(not(a and b)))
elif(res=='NOR'):
    print("Result =",int(not(a or b)))
    
    
