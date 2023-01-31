# Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. 
# Meaning that if the cubed number is over 1000 break the loop.

for i in range(1, 1001):

    cube = (i * i * i)
    if cube < 1001:
        print(cube)

    else:
        break



#Exercise #2
#Get first prime numbers up to 100

for num in range(1, 101):
    if num > 1:

        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#Exercise 3
#Take in a users input for their age, if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, else print seniors

age = int(input("What is your age? "))
if age < 18:
    print("You are a kid.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")