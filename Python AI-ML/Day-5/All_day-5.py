###data_structure.py : 

list1=[1,2,3,4,5]
print(type(list1))
print(list1)


list2=[13,124,'Faker',True]
print(type(list2))
print(list2)
list2[3]=False
print(list2)


null=[]
print(null)
null.append("bbg")
print(null)

listf=[12,23,1]
print(listf)
listf.insert(1, 100)
print(listf)
listf.remove(12)
print(listf)
listf.insert(0, 14)
print(listf)
for i in listf:
    print(i)
print(len(listf)) 
print(max(listf))
print(min(listf))
listf.sort()
print(listf)

#string slicing:

str1="student"
tr=str1[2:7:2]
print(tr)

val1="inserted"
print(val1[-9:9])

for i in range(1,20):
    print(i)
 
zx="Yugdeep"
print(zx.count)

#dict.py :
dict1={
    "Name":"Yugdeep",
    "Address": "Brt",
    "Roll no":"007"
}
print(type(dict1))
print(list(dict1.values()))
print(list(dict1.items()))

#addressing value in the dictionary :
print(dict1)
dict1["Address"]="Pokhara"
print(dict1)

for i,j in dict1.items():
    print(f"{i}:{j}")


parent_dict={
    1:{
        "name":"yugdeep"
    },
    2:{
        "name":"donna"
    }
}
print(parent_dict)

#sets.py  :

set1={1,"w",2,44,"gf","f"}
set2={1,12,2,24,22,}
print(set1.union(set2))
print(set2.difference(set1))
print(set1.isdisjoint(set2))

set1.intersection_update(set2)
print(set1)

set1.add(21)
print(set1)
set1.remove(1)
print(set1)

set1={1,2,3,(4,5,6),9}
set2={4,1,3,5,6,[7,8,9],10}

print(set1)
print(set2)



#ask user for input and put them in a list
'''count=0
inp_list=[]
asked=int(input("how many numbers you wanna enter?: "))
while count < asked:
    n=int(input("enter the number: "))
    inp_list.append(n)
    count+= 1
print(inp_list)'''

#a program to ask 5 numbers and perform the square of each number and store in another number
inp_list=[]
count=0
while count < 5:
    numbers=int(input("Enter the numbers: "))
    inp_list.append(numbers)
    count+= 1
print(f"The given list is {inp_list}")
square_list=[]
for i in inp_list:
    i=i**2
    square_list.append(i) 
print(f"The squared list of the numbers is {square_list}")
print(inp_list+square_list)

#ask user to input student name and class and store them in a dictionary
queue=int(input("How many student data do you want to enter?: "))
std_list={}
while queue>0:
    queue-=1
    inp_name=input("Enter Name: ")
    inp_class=int(input("Enter class: "))
    std_list[inp_name] = inp_class
print(std_list)

#'''tuple1=(1,2,3,4,5) #immutable :
li=[1,2,3,1] #mutable
tuple1[1]=8
print(tuple1)

li[1]=8
print(li)

tuple2=(4,2,1,2)
print(tuple1+tuple2)    

#packing and unpacking :


tpi=1,2,3
print(tpi)

a,b,c= tpi
print(a)
print(b)
print(c) 

li=[1,2,3,1,2,2,1]
print(li)
tp= tuple(li)
print(tp)
print(tp.count(2))

