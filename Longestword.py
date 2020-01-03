''' Create a function to return the longest word in a string '''

def max_len(l):
 max_len=len(list[0])
 index=0;
 j=0;
 for i in list:
  if(max_len<len(i)):
    index=j;
  j+=1;
 return index;  

ans=input("enter the string")
list=[]
list=ans.split(' ')
strg=max_len(list)
print("The longest word in the String",ans,"is ",list[strg])
    
