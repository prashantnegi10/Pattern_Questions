"""
ouput pattern

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
n=int(input('enter a no: '))
k=0
for i in range(1,2*n):
    if i<=n:
        k=k+1
    else:
        k=k-1
    for j in range(1,2*n):
        if(j>=n+1-k and j<=n-1+k):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
        