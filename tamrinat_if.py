from random import randint

number = int(input("enter a number : "))
joon = 3
if not 0 < number <= 10:
    print("Select between 1 to 10")
    exit 
while joon !=0:
    random = randint(1, 10) 
    if number != random :
        joon -= 1
        print("wrong guess! try again!...")
        number = int(input("enter a number : "))
    else:
        ("that's it!...")
