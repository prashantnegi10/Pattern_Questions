"""
output pattern
    *
   * *
  * * *
 * * * *
"""
n=int(input('enter a no: '))
for i in range(1,n+1):
    k=1
    for j in range(1,2*n):
        if(j>=n+1-i and j<=n-1+i and k):
            print("*",end=" ")
            k=0
        else:
            print(" ",end=" ")
            k=1
    print("\n")