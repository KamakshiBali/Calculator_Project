# This function adds two numbers
import Addition
import Subtraction
import Multiplication
import Division
import power
import square
import sqrt
import factorial
import math

# This is to present a menu to the user
print("Select operation.")
print("1.Addition")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Square")
print("7.Square root")
print("8.Factorial")


while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", Addition.add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Subtraction.subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Multiplication.multiply(num1, num2))

        elif choice == '4':
            try:
                print(num1, "/", num2, "=", Division.divide(num1, num2))
            except ZeroDivisionError:
                print("ZeroDivisionError! Please ensure second number is not 0")
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
      
    elif choice in ('6','7','8'):
        try:
            num=float(input("Enter number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '6':
            print("Square of", num, "=", square.square(num))
        elif choice == '7':
            print("Square root of", num, "=", sqrt.sqrt(num))
        elif choice == '8':
            print("Factorial of", num, "=", factorial.fact(num))
            
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
      
    elif choice == "5":
        try:
            num=float(input("Enter base: "))
            pow=float(input("Enter power: "))
            print(num, "raised to the power", pow, "=", power.power(num,pow))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")

