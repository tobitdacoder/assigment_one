average=0
count=0
total=0

while True:
   number=input("enter a number: ")
   if number=="done":
      break
      #this break here is breaking the loop while number is equal to "done"  
   else:
      #this else will be applied when the number is different to "done"
      
      try: #this is to handle the problen if we have an invalid input
         total+=float(number)
         count+=1
         average=total/float(count)
      except ValueError:
         print("invalid input")
         continue
print(f"the average is equal to {average}, the total = {total}, Count = {count}")