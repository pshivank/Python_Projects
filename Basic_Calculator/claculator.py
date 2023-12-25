def Calculator(num1 , num2 , opr ):
    if opr == '+':
        return num1 + num2
    
    elif opr == '-':
        return num1 - num2
    
    elif opr == '*':
        return num1 * num2 
    
    elif opr == '/':
        return num1 / num2 
    
    elif opr == 'e':
        return num1 ** num2


def main():
    num1 , opr , num2 = input("Enter Your Equation with spaces : -- ").split()
    result = Calculator(int(num1) , int(num2) , opr )
    print(result)

if __name__ == '__main__':
    main()

