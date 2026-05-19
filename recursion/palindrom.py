def palindrom(s, n, i=0):
    if n<i:
        return True
    if s[n]==s[i]:
        return palindrom(s, n-1, i+1)
    else:
        return False


s = "sacas"
n = len(s)-1
print(palindrom(s, n))
