arr = [15, -2, 2, -8, 1, 7, 10, 13] 

def len_of_arr(arr): 
    length = 0
    for i in range(len(arr)): 
        sum = 0
        for j in range(i, len(arr)): 
            sum += arr[j] 
            if sum == 0: 
                length = max(length, j-i + 1) 
  
    return length
  
print ("The max Length of subarray with sum 0 is % d" % len_of_arr(arr))