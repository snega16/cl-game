import random

answer=random.randint(1,20)
print("Iam guessing a number from 1 to 20")
count=0

while(True):
    count=count+1
    print("Can you guess it?")
    prediction=int(input())
    if prediction > answer:
        print("the answer is too high")
    elif prediction < answer:
        print("the answer is too low")
    else:
        print("It is correct")
        break
        
print("You have attempted for" + str(count) + "times")
