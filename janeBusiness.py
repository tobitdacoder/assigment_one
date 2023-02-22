'''Jane owns a money lending business called Save To Grow Credit that loans out money. A given client of this company is given a loan that has to be repaid in a month's time (30 days) or less days with 10% interest. If the client fails to pay at the end of 30 days, the client is charged a fine of 1% of the loan per day. Write a python application that determines the total amount that is paid by the client to the company after a given number of days'''


name=input("Enter client name: ")
amount=float(input("enter amount of loan: "))
days=int(input("enter the number of days: "))
total=0

interest=amount*(10/100)
#here the interest will specify how mush has to be added to the initial loan as the interest depending on the interest rule
if days <=30:
    total=amount+interest
    #here the "total" which means total amount that will be payed back with the interest while days are less than or equal to 30  
    print(f" client name: {name}")
    print(f"the loan is: {amount}")
    print(f"days spent: {days}")
    print(f"this the total ammount to pay: {total}")
elif days >30:
    #here its when the days are over 30 days which means that the interest will be changing according to the extradays spent by the loan taker 
   extradays=days-30
   fine=(1/100)*amount
   increasing=fine*extradays
   total=amount+interest+increasing
   print(f" client name: {name}")
   print(f"the loan is: {amount}")
   print(f"days spent: {days}")
   print(f"this the total ammount to pay: {total}")


   
   
   
   
   
    
    
   

