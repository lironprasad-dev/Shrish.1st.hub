#assignment operators:

a=175
 #modulus of a by 3
a%=13
print("modulus is: ", a)
#multiplication of a by 2
a*=2
print("multiplication is: ", a)
a+= a+4

#return false value if the user inputs default value such as 12345678 or password
passw=input("Enter your password: ")
defp = "12345678"
min_len=8
max_len=20
max_check=len(passw) < max_len
leng=len(passw)>=min_len
chek = (passw!=defp)
print(f" is it meeting the minimum length requirement? : {leng}")
print(f"is it something other than the default password? : {chek} ")
print(f"is it below the max lenght? : {max_check}")

#to calculate total bill to be paid of several units of items after dedecting discouunt and adding tax
import math
print("Discount for all items is 10% ")
print("Tax for all items is 13% ")
uni=int(input("Enter number of units purchased: "))
pri=float(input("Enter price per unit: "))
total=uni*pri
act=total-(total*0.10)
fin=float(act+(act*0.13))
print(f"Total bill to be paid after discount and adding tax is: {fin:.3f}")

#ask user to input password and if password length is less than 4 print add more chracters
passw=input("Enter your password: ")
if len(passw)<4:
    print("Add more characters to your password")   
else:
    print("Password accepted")
    
print("Length of your password is:", len(passw))

#same program as de2task.py but use different assignment operators

import math
#to calculate total bill to be paid of several units of items after dedecting discouunt and adding tax
import math
print("Discount for all items is 10% ")
print("Tax for all items is 13% ")
uni=int(input("Enter number of units purchased: "))
pri=float(input("Enter price per unit: "))
total=uni*pri
total-=(total*0.10) #applying discount using -= operator
total+=(total*0.13)     #adding tax using += operator
fin=float(total) #final amount
print(f"Total bill to be paid after discount and adding tax is: {fin:.3f}")