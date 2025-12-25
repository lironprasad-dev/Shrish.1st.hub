#truth table for and operator using python
print("Truth table for AND operator \n")
a= True
b= False
print(f"True AND True : {a and a}")
print(f"True AND False : {a and b}")
print(f"False AND True : {b and a}")
print(f"False AND False : {b and b}\n")
#truth table for or operator using python
print("Truth table for OR operator \n")
print(f"True OR True : {a or a}")
print(f"True OR False : {a or b}")
print(f"False OR True : {b or a}")
print(f"False OR False : {b or b}\n")
#truth table for not operator using python
print("Truth table for NOT operator \n")
print(f" NOT True : {not a}")
print(f" NOT False : {not b}")
#find out greater among a,b,c,d without using if-else
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))
d=int(input("Enter fourth number "))
a_great=(a>b) and (a>c) and (a>d)
b_great=(b>a) and (b>c) and (b>d)
c_great=(c>a) and (c>b) and (c>d)
d_great=(d>a) and (d>b) and (d>c)
print(f"Is a the greatest number? : {a_great}")
print(f"Is b the greatest number? : {b_great}")
print(f"Is c the greatest number? : {c_great}")
print(f"Is d the greatest number? : {d_great}")

###concept : 

l1=l2=[1,2,3]
print(l1 is l2 )

###
nme=input( "enter your name: ")
print("a" in nme)

###
#check even or odd without if else
num=int(input("Enter a number "))
even=(num %2) ==0
print(f"the number is even?: {even}")

###
#question 1
dest=input("Enter the destination: ") .lower()
price=int(input("Enter the price: "))
max_price=50000
book= price<=max_price and (not dest=="asia" ) 
print(f"Should I book the ticket: {book}")

#question 2
approved_ids=["A101", "B205", "C303", "0410"]
employee_id=input("Enter your employee ID: ").upper()
check=employee_id in approved_ids
print(f"the id is among the employees?: {check}")
print("The next id to be checked is Z9999")
usercheck= "Z9999" not in approved_ids
print(f"Z9999 is not among the employees?: {usercheck}")

#question 3
balance=1000
deposit=250
service_fee=10.50
interest=1.05
balance+= 250
balance-= 10.50
balance*=1.05
final_balance=balance 
print(f"Final account balance: {final_balance:.3f}")
balance//=100
print(f"Approximate number of shares that can be bought: {balance}")



