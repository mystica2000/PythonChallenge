print("\n enter the input")
symbol=input()
a=symbol[0]
b=symbol[1:]
print(a)
print(b)
if(a=='+' or a=='-' or a=='*' or a=='/'):
    print('\n',a,'|')
    for(i=0;i<len(b)+1;i++):
        print(i)
else:
    print("\n expression invalid")
