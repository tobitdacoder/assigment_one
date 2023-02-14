a=[1,4,6,8,12,15]
target=15

def binary_search(a,target,start,stop):
    
   min=start
   max=stop-1
   while min<=max:
      mid=(min+max)//2
      if a[mid]<target:
         min=mid+1
      elif a[mid]>target:
         max=mid-1
      else:
         return mid
   return -(min+1)
print(binary_search(a,target,0,len(a)))
#this is a program that return us the index of the target using binnary search