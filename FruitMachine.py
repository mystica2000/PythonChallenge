'''Fruit Machine Write a program to simulate a Fruit Machine that displays three symbols at random from Cherry, Bell, Lemon, Orange, Star, 
Skull. The player starts with £1 credit, with each go costing 20p. If the Fruit Machine “rolls” two of the same symbol, the user wins 50p. 
The player wins £1 for three of the same and £5 for 3 Bells. The player loses £1 if two skulls are rolled and all of his/her money if 
three skulls are rolled.The player can choose to quit with the winnings after each roll or keep playing until there is no money left.'''

import random

print("\n Let's play a game")

credit=1;
contin='Y'
fruit={0:'cherry',1:'Bell',2:'Lemon',3:'Orange',4:'Star',5:'Skull'}
while(credit!=0):
 print("\n Rolling wait")
 flag=0;
 a=random.randint(0,5)
 b=random.randint(0,5)
 c=random.randint(0,5)
 print(fruit[a],"-",fruit[b],"-",fruit[c])
 if(a==b==c==5):
    credit=0;
 elif((a==b==5)or(a==c==5)or(c==b==5)):
    credit=credit-1;
 elif((a==b)or(a==c)):
     flag=1;
     credit=credit+0.50;
 elif(a==b==c==1):
     flag=1;
     credit=credit+5;
 elif(a==b==c):
     flag=1;
     credit=credit+1;
     
 print("\n the credit amount=",credit)
 if(flag==1):
     print("\n Do u wanna continue Y/N")
     str=input()
     if(str=='Y'):
         continue;
     else:
         print("\n Your amount is",credit)
         break;
 else:
     credit=credit-0.50;
     continue;
     
