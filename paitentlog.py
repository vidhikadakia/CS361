import datetime

def gettime():
    return datetime.datetime.now()

def user_input(n):
    if n == 1:
        value = input("Type here the foods you had today\n")
        with open('patient1-food.txt', 'a') as op:
            op.write(str([str(gettime())])+": " + value + "\n")
            print("Successfully saved 😊")

    elif n == 2:
        value = input("Type here the foods you had today\n")
        with open('patient2-food.txt', 'a') as op:
            op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully saved 😊")
    elif n == 3:
        value = input("Type here the foods you had today\n")
        with open('patient3-food.txt', 'a') as op:
            op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully saved 😊")

    else:
        print("Please enter a valid input(1 for Paitent1, 2 for Paitent2, and 3 for Paitent3)")

def retrieve(n):
    if n == 1:
        with open ("patient1-food.txt") as op:
            for i in op:
                print(i, end = "")

    elif n ==2:
        with open("patient2-food.txt") as op:
            for i in op:
                print(i, end="")


    elif n ==3:
        with open("patient3-food.txt") as op:
            for i in op:
                print(i, end="")
    else:
        print("The file doesn't exist. ")

print("Health Management System: ")
a = int(input("Press 1 for saving a value and 2 for retriving --- "))

if a ==1:
    b = int(input("Press 1 for Patient1, 2 for Paitent2 , 3 for Patient3 -- "))
    user_input(b)
else:
    b = int(input("Press 1 for Patient1, 2 for Patient2, 3 for Patient3 -- "))
    retrieve(b)







