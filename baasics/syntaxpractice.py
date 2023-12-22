a=input("Enter your name : ")
age=int(input("Enter your age : "))
list=[]
if a.length()>=4 and age>=18: 
    list.append(a)
    list.append(age)
else:
    print("Invalid input")
print(list)
print(type(list))


