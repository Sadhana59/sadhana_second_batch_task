
a = [1 , 2 , 3 , 4 , 5]
k = 3
n = len(a)
q = n//k
r =n%k
i = 0
output_array = []
while i<q:
    start = i*k
    end = (i + 1) * k
    t = a[start:end]
    t = t[::-1]
    output_array = output_array + t
    i = i + 1

if r!=0:
    t = a[q * k:]
    t = t[::-1]
    output_array = output_array + t
print(output_array)




#second method using formula

 
def reverse(arr, n, k): 
    i = 0
    while(i<n): 
      
        left = i  
        right = min(i + k - 1, n - 1)  
  
        #reversing iteration
        while (left < right): 
            arr[left], arr[right] = arr[right], arr[left] 
            left+= 1; 
            right-=1
        i+= k 
       
arr = [1, 2, 3, 4, 5, 6, 7, 8]
n = len(arr)                   
k = 3
n = len(arr)  
reverse(arr, n, k) 
print(arr)
    
