import random
#function which return tuple of 2 random numbers
def rand():
    return((random.randint(1,7),random.randint(1,7)))  #returning tuple of 2 random numbers

num1,num2 = rand() #assigining both number to num1 and num2

ans = int(input("How much is "+str(num1)+" times "+ str(num2)+"? "))#asking user to enter answer
#looping until answer is correct
while(ans != num1 * num2):
    ans = int(input("Please try again")) #printing wrong answer

print("Done!") #printing Done
