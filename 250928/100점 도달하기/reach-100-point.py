N=int(input())
while N<=100:
    if N>=90:
        print("A",end=' ')
    elif N >=80:
        print("B",end=' ')
    elif N>=70:
        print("C",end=' ')
    elif N>=60:
        print("D",end=' ')
    elif N<60:
        print("F",end=' ')
       
    N=N+1
    if N ==101:
        break

