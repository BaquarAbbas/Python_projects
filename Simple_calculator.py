import math

def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def Divide(a,b):
  return a / b

def sqrt(a):
  result = math.sqrt(a)
  return result

def exp(a):
  return a ** 2

def sin(x):
  result = math.sin(x)
  return result

def cos(x):
  result = math.cos(x)
  return result

def tan(x):
  result = math.tan(x)
  return result


print("""
choose a number for the following operations:
1 - Addition(x,y)
2 - subtraction(x,y)
3 - Multiply(x,y)
4 - Divide(x,y)
5 - square(x)
6 - squareroot(x)
7 - sin(x)
8 - cos(x)
9 - tan(x)""")

op = int(input("Enter a operation to perform!"))
while op < 10:
    if op == 1:
      print("Enter parameters")
      x1 = int(input("enter x:"))
      y1 = int(input("enter y:"))
      res1 = add(x1,y1)
      print("Adddition = ",res1)
    elif op == 2:
      print("Enter parameters")
      x2 = int(input("enter x:"))
      y2 = int(input("enter y:"))
      res2 = subtract(x2,y2)
      print("subtraction = ",res2)
    elif op == 3:
      print("Enter parameters")
      x3 = int(input("enter x:"))
      y3 = int(input("enter y:"))
      res3 = multiply(x3,y3)
      print("Multiplication = ",res3)
    elif op == 4:
      print("Enter parameters")
      x4 = int(input("enter x:"))
      y4 = int(input("enter y:"))
      res4 = Divide(x4,y4)
      print("Division = ",res4)
    elif op == 5:
      print("Enter parameters")
      x5 = int(input("enter x:"))
      res5 = exp(x5)
      print("Square of number = ",res5)
    elif op == 6:
      print("Enter parameters")
      x6 = int(input("enter x:"))
      res6 = sqrt(x6)
      print("Square root of number = ",res6)
    elif op == 7:
      print("Enter parameters")
      x7 = int(input("enter x:"))
      res7 = sin(x7)
      print("sin(x) = ",res7)
    elif op == 8:
      print("Enter parameters")
      x8 = int(input("enter x:"))
      res8 = cos(x8)
      print("cos(x) = ",res8)
    elif op == 9:
      print("Enter parameters")
      x9 = int(input("enter x:"))
      res9 = tan(x9)
      print("tan(x) = ",res9)
    else:
      print('Choose another operation')
    new = int(input("do you want to continue ? - (Yes-1) , (No-0)")) 
    if new == 1:
      op = int(input("Enter operation"))
    elif new == 0:
      print("Thanks for using Scientific-Calculator!")
      break     
