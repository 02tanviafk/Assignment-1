#ASSIGNMENT 1


#Tuple
tup=(1,2,3,4)
tup1=list(tup)
tup1.append(5)
tup1.remove(1)
print(tup1)



#dictionary

dict={"name":"Tanvi","age":18,"city":"Pune"}
print(dict["age"])
print(dict)
print(dict.pop("age"))
print(dict)
dict["clg"]="mit wpu"
print(dict)

#ASSIGNMENT 2

a=int(input("enter no. 1:"))
b=int(input("enter no. 2:"))
c=int(input("enter no. 3:"))
if(a>b and a>c):
 print("the greatest no. is",a)
elif(b>a and b>c):
    print("the greatest no. is",b)
else:
    print("the greatest no. is",c)


#ASSIGNMENT 3


# Function to check if the sides form a right-angled triangle
def is_right_triangle(side1, side2, side3):

    sides = sorted([side1, side2, side3])
    
  
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    return False


try:
    a = float(input("Enter the length of the first side: "))
    b = float(input("Enter the length of the second side: "))
    c = float(input("Enter the length of the third side: "))

    if (a + b > c) and (a + c > b) and (b + c > a):
    
        if is_right_triangle(a, b, c):
            print("\nResult: The given sides form a Right-Angled Triangle.")
        else:
            print("\nResult: The given sides DO NOT form a Right-Angled Triangle.")
    else:
        print("\nError: The given sides cannot form a valid triangle.")

except ValueError:
    print("Invalid input! Please enter numeric values only.")
    
    
#ASSIGNMENT 4
import numpy as np
A=np.array([[1,2],
           [3,4]])
B=np.array([[5,6],
           [7,8]])
c=A+B
print("Matrix A: ")
print(A)
print("Matrix B: ")
print(B)
print("Addition of two matrices: ", c)


#assignment 5

import re
string=input("enter a string:")
if re.fullmatch(r'[a-zA-Z0-9]+' , string):
    print("string contains a-z A-Z 0-9")

else:
    print("string contains other characters")
