b=5
a=5
if (a==b):
    print(a==b)


### de1.py : 
# # #comments and
'''multi line 
commment '''

"""fj 

neverthelesss
"""
 #multiline print
print("""biratnagar
 morang
  """)

# # #variables
name="Yugdeep"
roll=121
place="mt rushmore"

#  \n should be in the same line as the print statement
print(name, roll,"\n",place)  


#for different variables to have same value
# i.e a=50, b=50 and c=50
x=y=z=75
a,b,c=25,40,24
h,g,i=30,53,23
print(a,b,c)
print(h,g,i)
print(x,y,z)
 

           
#value interchange :

fname="Yugdeep" 
lname="Koirala"
fname,lname=lname,fname
print(fname,lname)

#data types
a=True
b=2
c=3.4
d=4-7j
e='tjt'
print(type(a))
print("type of b", type(b))


#type casting
c=str(e)
print("type of c ",type(c))
first="1234"
sec=int(first)
print(sec+b)

#input/output

pi=input("Enter name: ")
print(pi,"ullala")

#formatted string
fi=input ("Enter the fname ")
la=input("enter the name ")
print(f"yes {fi} {la}")




#del1task.py :
import math
#different caclulations between two numbers
num1=int(input("Enter first number "))
num2=int(input("Enter second number "))
print("Addition ", num1+num2)
print("Subtraction ", num1-num2)
print("Multiplication ", num1*num2)
print("Division ", num1/num2)
print("Floor Division ", num1//num2)
print("Modulus ", num1%num2)
print("Exponent ", num1**num2) 


#program to convert age into months
x=int(input("enter age: "))
y= 12*x
print("Estimated months of the user is: ",y)

