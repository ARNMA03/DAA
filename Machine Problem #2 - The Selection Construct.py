"""Create an algorithm that allow end-user to choose from
{a} addition, {s} subtraction,
{m} multiplication and {di} division.
After selection was made, the end user needs to input 2 numbers
and display the correct answer based on the selection made."""
while True:
    op = input("""
    Operations:
    (a) Addition,
    (s) Subtraction,
    (m) Mutiplication,
    (di) Division
    Enter operation: """)


    if op == "a" or op == "s" or op == "m" or op == "di":
            user1 = int(input("\tInput first number: "))
            user2 = int(input("\tInput second number: "))
            if op == "a":
                print(f"\tthe sum of first and second input is {user1+user2}")
                break
            elif op == "s":
                print(f"\tthe difference of first and second input is {user1-user2}")
            elif op == "m":
                print(f"\tthe product of first and second input is {user1*user2}")
                break
            elif op == "di":
                if user2 == 0:
                    print("\tInvalid it is undefined!")
                else:
                    print(f"\tthe quotient of first and second input is {user1/user2}")
                break
    else:
        print("\tInput a valid operation!")
