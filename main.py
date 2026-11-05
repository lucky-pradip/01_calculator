try:
    a=int(input("Enter first number: "))
    b=int(input("Enter first number: "))

    print("What kind of operation do you want to perform. Press + for addition\nPress - for Subtraction\nPress / for divition \n * for multiplication")

    o=input("Enter Operation: ")
    match o:
        case "+":
            print(f"The result is: {a+b}")
        case "-":
            print(f"The result is: {a-b}")
        case "*":
            print(f"The result is: {a*b}")
        case "/":
            print(f"The result is: {a/b}")

except Exception as e:
    print("Enter a valid value of a and b")
