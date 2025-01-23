prev = 0


def calc():
    global prev
    if op == "a":
        answer = f"\tthe sum of first and second input is {user1+user2}"
        prev = user1+user2
        print(answer)
    elif op == "s":
        answer = f"\tthe difference of first and second input is {user1-user2}"
        prev = user1-user2
        print(answer)
    elif op == "m":
        answer = f"\tthe product of first and second input is {user1*user2}"
        prev = user1*user2
        print(answer)
    elif op == "di":
        if user2 == 0:
            print("\tInvalid it is undefined!")
        else:
            answer = f"\tthe quotient of first and second input is {user1/user2}"
            prev = user1/user2
            print(answer)


while True:
    op = input("""
    Operations:
    (a) Addition,
    (s) Subtraction,
    (m) Mutiplication,
    (di) Division,
    (no) You dont want to continue
    Enter operation: """).lower()
    if op == "no":
         print("\texiting...")
         break
    elif prev != 0:
        if op == "a" or op == "s" or op == "m" or op == "di":
            user1 = prev
            user2 = int(input("\tInput second number: "))
            calc()
        else:
            print("\tInput a valid operation!")
    elif prev == 0:
        if op == "a" or op == "s" or op == "m" or op == "di":
            user1 = int(input("\tInput first number: "))
            user2 = int(input("\tInput second number: "))
            calc()
        else:
            print("\tInput a valid operation!")
