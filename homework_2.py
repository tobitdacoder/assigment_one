
name=input("enter your name: ")
age=int(input("enter your age: "))
print(f"hello{name}, you are {age} years old") 

list=[]
for i in range(5):
   number=int(input("enter a number: "))
   list.append(number)
finalSum=0  
for number in list:  
   if number%2==0:
      finalSum+=number
print(finalSum)
#here we are creating a program which appends values in the list and then after we add the specified values added in the list if those values are even (divisible by 2 without any reminder)
# 
      
   
   
