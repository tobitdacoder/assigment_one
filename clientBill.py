#QUESTION 3:

ChipsAndChicken=10000
matokeAndBeef=8000
print("\n")
print("1. ChipsAndChicken 🍗")
print("2. matokeAndBeef 🥩\n")
order=int(input("what is your order sir?: "))
number=int(input("how many plates do you need?: "))

print("\n")
match order:
   case 1:
      facture=ChipsAndChicken*number
      print("the bill is"+" "+str(facture)+" "+ "UGX sir")
   case 2:
      facture=matokeAndBeef*number
      print("the bill is"+" "+str(facture)+" "+ "UGX sir")
   case _:
      print("invalid order")
print("\n")

print("yes")
print("No")

beverage=str(input("any beverage 🍹?: "))
print("\n")
if beverage=="yes":
   mango=2000
   pineaple=2500
   passion=1800
   cocoa=3500
   print("1.mango juice 🥤")
   print("2.pineaple juice 🍸")
   print("3.passion juice 🧋")
   print("4.cocoa juice 🥛\n")
   
   choice=int(input("which one sir?: "))
   number_=int(input("how many cups?: "))
   print("\n")
   
   
   match choice:
      case 1:
         facture2=mango*number_
         print(f"it will cost {facture2} for the beverage sir")
      case 2:
         facture2=pineaple*number_
         print(f"it will cost {facture2} for the beverage sir")
      case 3:
         facture2=passion*number_
         print(f"it will cost {facture2} for the beverage sir")
      case 4:
         facture2=cocoa*number_
         print(f"it will cost {facture2} for the beverage 🍹 sir")
      case _:
         print("invalid choice")
   total=facture+facture2
   print("\n")
   print(f"the total bill will be equal to {total} UGX sir😁")
   
elif beverage=="no":
   print("thank you sir")
   total=facture
   print(f"the total bill will be equal to {total} UGX sir😊")