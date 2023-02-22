average=0
count=0
total=0

while True:
   number=input("enter a number: ")
   if number=="done":
      break
   else:
      try:
         total+=float(number)
         count+=1
         average=total/float(count)
      except ValueError:
         print("invalid input")
         continue
print(f"the average is equal to {average}")