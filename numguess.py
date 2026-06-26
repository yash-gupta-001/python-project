import random
a=random.randint(1,100)
user=int(input("Enter The Number :  "))
attempt=0
while (a!=user):
    
    attempt+=1
    user=int(input("You entered the Wrong number , Guess again "))
    if(a<user):
        print('Too High')
    elif(a>user):
        print("Too Low")
    else:
        print("you won",attempt)
       