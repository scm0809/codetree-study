A,B= map(int,input().split())
X=0
for i in range(A,B):
    if i%2==1:
        continue
    else:
        X=X+i
print(X)