## Rock,Paper,Scissor Game


'''
1.stone >sessior>paper>stone
2.paper <seccior<stone<paper
3.scissor
'''
'''
import random
com=random.choice([1,2,3])
youstr=input("enter your choice  :   ").upper()
yd={"R":1,"P":2,"S":3}
rd={1:"Rock",2:"paper",3:"scissor"}

you = yd[youstr]
#com=yd[comp]
print("your choice :   ",rd[you])
print("computer choice   :  ",rd[com])


if(com==you):
    print("it's  a  TIE")
else:
    if(com==1 and you==2):
        print("YOU  WIN!!")
    elif(com==1 and you==3):
        print("YOU  LOSE!!") 
    elif(com==2 and you==1):
        print("YOU  LOSE!!")                            
    elif(com==2 and you==3):
        print("YOU  win !!")       
    elif(com==3 and you==1):
        print("YOU  win!!") 
    elif(com==3 and you== 2):
        print("YOU  LOSE!!") 
    else:
        print("ERROR 404:  something went wrong")    '''
'''1.snake
2.water 
3.gun'''

import random
com=random.choice([1,2,3])
ys=input("enter your choice   :   ").upper()
choi={"S":1,"W":2,"G":3}
cort={1:"snake",2:"water",3:"gun"}
you=choi[ys]

print(f"your choice  :  {cort[you]}  ")
print(f"computer choice  :  {cort[com]}")
print("")

if (com==you):
    print("it's  a  tie   ")
else:
    if(com==1 and you==2):
        print("YOU  LOOSE !! ")
    elif(com==1 and you==3)    :
        print("YOU  WIN !!")
    elif(com==2 and you==1)    :
        print("YOU  WIN !!")   
    elif(com==2 and you==3)    :
        print("YOU  LOSE !!") 
    elif(com==3 and you==1)    :
        print("YOU  LOSE !!")   
    elif(com==3 and you==2)    :
        print("YOU  WIN !!")   
    else:
        print("ERROR 404: SOMETHING WENT WRONG !!")

print("")
print("")
