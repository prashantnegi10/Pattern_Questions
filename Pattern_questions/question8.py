"""
output pattern
*                  *
* *              * *
* * *          * * *
* * * *      * * * *
* * * * *  * * * * *

"""
n=int(input('enter a no: '))
for i in range(1,n+1):
    for j in range(1,2*n+1):
        if(j<=i):
            print("*",end="")
        else:
            print(" ",end="")
        if(j>=2*n+1-i):
            print("*",end="")
        else:
            print(" ",end="")
    print("\n")