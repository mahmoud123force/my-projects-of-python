print("welcome to the simple calculator project in python")#ana hena br7b bl user
def g(x,y):#function ll gm3
    return x + y
def s(x,y):#function ll tar7
    return x - y
def m(x,y):#function ll drb
    return x * y
def d(x,y):#function ll qsm
    if y == 0:
        return "Error! Division by zero."
    return x / y
def p(x,y):#function ll power
    return x ** y
def r(x):#function ll square root
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    return x ** 0.5






while True:
 choice2 =str(input("numbers A. real numbers\nB. decimal numbers\n C.complex numbers\n"))                   
 choice= str(input("Enter your choice: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Power\n6. Square Root\n"))
 if choice2.lower() == 'a' or choice2.upper() == 'A':
  if choice== '1':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", g(a, b))
  elif choice== '2':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", s(a, b))
  elif choice== '3':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", m(a, b))
  elif choice== '4':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", d(a, b))
  elif choice== '5':
    a = int(input("Enter base number: "))
    b = int(input("Enter exponent: "))
    print("Result:", p(a, b))
  elif choice== '6':
    a = float(input("Enter number to find square root: "))
    print("Result:", r(a))
  else:
    print("Invalid choice! Please select a valid operation.")
 elif choice2.lower() == 'b'or choice2.upper() == 'B':
   if choice== '1':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", g(a, b))
   elif choice== '2':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", s(a, b))
   elif choice== '3':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", m(a, b))
   elif choice== '4':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", d(a, b))
   elif choice== '5':
    a = float(input("Enter base number: "))
    b = float(input("Enter exponent: "))
    print("Result:", p(a, b))
   elif choice== '6':
    a = float(input("Enter number to find square root: "))
    print("Result:", r(a))
   else:
    print("Invalid choice! Please select a valid operation.")
 elif choice2.lower() == 'c' or choice2.upper() == 'C':  
  if choice== '1':
    a = complex(input("Enter first number: "))
    b = complex(input("Enter second number: "))
    print("Result:", g(a, b))
  elif choice== '2':
    a = complex(input("Enter first number: "))
    b = complex(input("Enter second number: "))
    print("Result:", s(a, b))
  elif choice== '3':
    a = complex(input("Enter first number: "))
    b = complex(input("Enter second number: "))
    print("Result:", m(a, b))
  elif choice== '4':
    a = complex(input("Enter first number: "))
    b = complex(input("Enter second number: "))
    print("Result:", d(a, b))
  elif choice== '5':
    a = complex(input("Enter base number: "))
    b = complex(input("Enter exponent: "))
    print("Result:", p(a, b))
  elif choice== '6':
    a = complex(input("Enter number to find square root: "))
    print("Result:", r(a))
  else:
    print("Invalid choice! Please select a valid operation.")
 choice3 = str(input("Do you want to continue? (yes/no): "))
 if choice3.lower() == 'no' or choice3.upper() == 'NO':
    print("Thank you for using the simple calculator!")
    break
print("Thank you for using the simple calculator!")
