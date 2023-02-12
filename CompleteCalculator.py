#QUESTION 9:

fnum=int(input("first number: "))
snum=int(input("second num: "))

print("\n")
print("* : multiplication")
print("/ : division")
print("+ : addition")
print("- : substraction\n")

opperator=str(input("chose an opperator:"))

match opperator:
   case "*":
      print(f"the result is {fnum*snum}")
   case "/":
      if snum==0:
         print("impossible")
      else:
         print(f"the result is {fnum/snum}")
   case "+":
      print(f"the result is {fnum+snum}")
   case "-":
      print(f"the result is {fnum-snum}")
   case _:
      print("this opperator does not exist !!!")