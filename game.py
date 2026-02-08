import random
a=random.randrange(1,100)
number=-1
guess=0
while (a!=number):
    
    guess+=1
    number=int(input("enter a number to guess:"))
    if(number<a):
      print("higher")
    elif(number>a):
     print("lesser")
   


print(f"you guessed correctly in {guess} attempt.")
    
