x = int(input("Num1 = "))
y = int(input("Num2 = "))
oper = input("Enter operator \n1. + \n2. - \n3. * \n4. /\n: ")

match oper:
    case '+':
        print(x + y)
        
    case '-':
        print(x - y)
        
    case '*':
        print(x * y)
        
    case '/':
        print(x / y)
        
    case _:
        print("Invalid")
