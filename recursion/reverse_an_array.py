def reverse_arr(rev, i, length):
    if i==length:
        return rev
        
    a = rev[i]
    rev[i] = rev[length]
    rev[length] = a
    
    return reverse_arr(rev, i+1, length-1)
    


arr = [1,2,3,4,9]
n = len(arr) - 1
print(reverse_arr(arr, 0, n))
