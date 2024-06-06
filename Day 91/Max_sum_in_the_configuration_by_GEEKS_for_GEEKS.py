def max_sum(a,n):
    #code here
    array_sum = sum(arr)
    current_sum = sum(i * arr[i] for i in range(n))
    
    max_sum = current_sum
    
    for i in range(n):
        current_sum = current_sum - array_sum + n * arr[i]
        max_sum = max(max_sum, current_sum)
    return max_sum
