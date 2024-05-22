# https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/roy-and-symmetric-logos-1/?filter=all&sort=most-likes

# the below line indicates  a string of digits as input, converts each digit to an integer, creates a list of these integers, and appends it to the list l1.
# l1.append(list(map(int,str(input())))) 

# if map er vitore split function nei taile all letter will take upto space but jodi na use kari taile alada every character list a convert habe .

# matrix or 2d array insert 



l1=[]
t = int(input())
while t>0:
    n = int(input())
    flag=1
    l1=[]
    
    for i in range(n):
        k1 =list(map(int,input()))
        l1.append(k1)
        
    for i in range(n):
        for j in range(n):
            if l1[i][j]!=l1[i][n-j-1] or l1[i][j]!=l1[n-i-1][j]:
                flag =0
    if flag==0:
        print("NO")
    else:
        print("YES")
        
            
              
    t-=1

