"""Create an algorithm that allow end-user to input 2 numbers and display its sum, difference, product and quotient."""


user1 = input("Input first number: ")
user2 = input("Input second number: ")
if user1.isalpha() or user2.isalpha():
    print("Invalid input!")
else:
    user1 = int(user1)
    user2 = int(user2)
    print(f"the sum of first and second input is {user1+user2}")
    print(f"the difference of first and second input is {user1-user2}")
    print(f"the product of first and second input is {user1*user2}")
    if user2 == 0:
        print("Invalid it is undefined!")
    else:
        print(f"the quotient of first and second input is {user1/user2}")
