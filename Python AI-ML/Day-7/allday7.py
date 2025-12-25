#args and kwargs
'''
def func(*arg):
    print(f"The arg are {arg[0]}")
    print(f"The arg are {arg[1]}")
    print(f"The arg are {arg[2]}")

func(1021,"nig",21)'''

'''def cles(*arg):
    sum=0
    for i in arg:
        sum=sum+i
    print(sum)

cles()
cles(12,11)
cles(123,121,22)
cles(11,10,15,13,9,7)'''

'''def function(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

function(name="Ulla", place="brt", religion="muhammed", Class= 11)''' 

def my_func(*arg,**kwarg):
    for i in arg:
        print(i)
    for i,j in kwarg.items():
        print(f"{i}:{j}")

my_func("shrish", city="brt", state="koshi", country="nepal")

#Exception handling :
'''s=int("")

print(s)
'''

'''a=45
b='123'
print(a+b)
'''

'''a=76
b=0
print(a/b) '''

try: #place risky code
    s=int("hello")
    print(s)
    print(type(s))
except: # run back statement
   print("exception occured")
finally: #runs code anyhow
      print("code ended")

# a program to ask two numbers from user and perform division operation :
try:
    num1=int(input("enter number: "))
    num2=int(input("enter another number: "))
    div=float(num1/num2)
except ValueError :
    print("Value error occured")
except TypeError:
    print("type error occured")
except ZeroDivisionError:
    print("Zero div occured")
else:
    print(f"{div:.3f}")
finally:
    print("program performed")

