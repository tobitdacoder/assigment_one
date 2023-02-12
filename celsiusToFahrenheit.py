#QUESTION 8:

def convert():
   celsius=float(input("give me any temperature in celsius: "))
   fahrenheit=(celsius*(9/5))+32 #assuming that to pass from celsius to fahrenheit we add 276  
   
   return f"{celsius} celsius degree is equal to {fahrenheit:.2f} in fahrenheit degree"
converted=convert()
print(converted)

def convert2():
   fahrenheit=float(input("give me any temperature in fahrenheit: "))
   celsius=(fahrenheit-32)*(5/9) #assuming that to pass from fahrenheit to celsius we substract 276  
   
   return f"{fahrenheit} fahrenheit degree is equal to {celsius:.2f} in celsius degree"
converted=convert2()
print(converted)