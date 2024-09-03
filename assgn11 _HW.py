x = int(input("Enter num1: "))
y = int(input("Enter num2: "))

print(f"x = {x}, y = {y}")
print("Enter operator from these [+, -, *, /, **]")
op = input()

if op in ('+', '-', '*', '/', '**'):
    if (op == '+'):
        print(x + y)
    elif (op == '-'):
        print(x - y)
    elif (op == '*'):
        print(x * y)
    elif (op == '/'):
        print(x / y)
    elif (op == '**'):
        print(x ** y)

else:
    print("Enter proper operator")

