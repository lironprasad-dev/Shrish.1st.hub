### Program to check if a student has passed or failed based on marks and assign grades accordingly
std_marks=float(input("Enter the marks of the student: "))
check= std_marks>=50
if check==False:
    print(f"The student has failed ")
elif check==True:
    print(f"The student has passed")
    if std_marks>=90:
        print(f"The student has obtained A grade")
    elif std_marks>=80 and std_marks<90:
        print("The student has obtained B grade")
    elif std_marks>=70 and std_marks<80:
        print("The student has obtained C grade")
    else:
        print("The student has obtained D grade")
else:
    print("Enter a valid mark")


### Program to check if a number is even, divisible by 5, or neither
num=int(input("enter a number: "))  
if num%2==0:
    print(f"{num} is even")
elif num%5==0:
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is neither even nor divisible by 5") 

a=17
if a > 10:
    print("a is greater than 10")

#ask user for input and execute the block only if the name entered is your name
nem=input("Enter your name: ").lower()
if nem:
    if nem=="yugdeep":
        print("Welcome Yugdeep!")

#ask user amt to be paid and if amt is >1000 compute the discount of 10% and calculate the actual amt to be paid otherwise just print the amt
amt=float(input("Enter the amount to be paid: "))
greater=amt>1000
if greater==True:
    discount=amt*0.10
    actual_amt=amt-discount
    print(f"Amount to be paid after discount: {actual_amt:.2f}") 
if greater==False:
    print(f"Amount to be paid: {amt:.2f}")

# to check whether the number is positive, negative or zero
num=int(input("enter a number: "))
if num>0:
   print(f"{num} is positive")
elif num<0:
 print(f"{num} is negative")
else:
 print(f"{num} is zero")

#to check larger among 3 numbers
a=int(input("enter number: "))
b=int(input("enter number: "))
c=int(input("enter number: "))
if a>=b>=c:
    print(a," is greatest")
elif b>=c:
    print(b," is greatest")
else:
    print(c, " is greatest")



    