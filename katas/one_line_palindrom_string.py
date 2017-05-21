def palindrome(n, c):return (n-len(c))*c[0]+c+c[::-1]+(n-len(c))*c[0] 
