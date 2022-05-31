def add(a , b):
    return a + b


def sub(a , b):
    return a - b


def multi(a , b):
    return a * b


def div(a , b):
    try:
        return a / b
    except Exception as error:
        print(error)


def pow(a , b):
    return a ** b


def remainder(a , b):
    return a % b

def select_op(choice):
    if choice == '#':
        return -1
    elif choice == '$':
        return 0
    elif choice in ('+', '-', '*', '/', '^', '%'):
        while True:
            fNo = str(input("Enter first number: "))
            print(fNo)
            if fNo.endswith('$'):
                return 0
            if fNo.endswith('#'):
                return -1

            try:
                num1 = float(fNo)
                break
            except:
                print("Not a valid number,please enter again")
                continue

        while True:
            sNo = str(input("Enter second number: "))
            print(sNo)
            if sNo.endswith('$'):
                return 0
            if sNo.endswith('#'):
                return -1
            try:
                num2 = float(sNo)
                break
            except:
                print("Not a valid number,please enter again")
                continue

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multi(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", div(num1, num2))
        elif choice == '^':
            print(num1, "^", num2, "=", pow(num1, num2))
        elif choice == '%':
            print(num1, "%", num2, "=", remainder(num1, num2))
        else:
            print("Something Went Wrong")
    else:
        print("Unrecognized operation")


while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice) == -1):
        print("Done. Terminating")
        exit()