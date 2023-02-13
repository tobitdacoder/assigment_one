#QUESTION 2:

def login():
   
   gmail="martha@gmail.com"
   password="martha"
   passwords=""
   
   account=str(input("enter your gmail here: "))  
   
   while account!=gmail:
      print("invalid account🤨")
      account=str(input("enter your gmail here: "))
      
   passwords=str(input("enter your password here: "))  
   while account==gmail and passwords!=password:
      print("invalid password😢")
      passwords=str(input("enter your password here: "))
   print("welcome to your account dear martha 😊")
      
login()