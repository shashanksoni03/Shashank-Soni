#Arithmeticoperators
a = 5
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) 

#Relational operators/Comparison Operators
a=50
b=20
print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)

#Assignment Operators
num = 10 
num=num+10
print(num)

num = 10
num+=10
print("num:",num)

num = 30
num-=20
print("num:",num)

#Logical Operators
print(not False)
print(not True)

a = 50
b = 20
print(not a>b)

val1 = True
val2 = False
print("and operator:", val1 and val2)

val1 = True
val2 = True
print("and operator:",val1 and val2)

# Type Conversion
a = 2
b = 4.25
sum = a+b
print(sum)

a = "2" 
b = 4.25
#print(a+b) #error

#Type Casting
a = int(2)
b = (4.25)
print(type(a)) 
print(a+b)

a = 2
b = float("4.25")

print(type(b))
print(a+b)

#Input in Python
input("Enter your Name :")

name = input("Enter your name:")
print("Welcome:",name)

age = input("enter your age:")
print("your age is:",age)

val = input("enter some value:")
print(type(val),val)

name = input("enter your name:")
age =  input("enter your age:")
marks = input("enter your marks:")

print("Welcome:",name)
print("age:",age)
print("marks:",marks)

#Let's Practice
first = int(input("first cnumber:"))
second = int(input("second number:"))

print("sum = ",first+second)

side = float(input("enter square side:"))
print("square:",side*side)
