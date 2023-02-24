
name=input("enter your name: ")
age=int(input("enter your age: "))
print(f"hello {name}😁, you are {age} years old!") 

#this is a very simple and basic python program that will print a string containing a name and a age that will be provided by the user 😁

#######################################################
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
      
list=[]
for i in range(8):
   string=input("enter a word: ")
   list.append(string)
finalist=[]  
for string in list:  
   if len(string)>5:
      finalist.append(string)
print(finalist)

#this is a Python program that takes a list of strings as input and returns a new list that
#contains only the strings with length greater than 5 . This code can be made more rich and complex

   
