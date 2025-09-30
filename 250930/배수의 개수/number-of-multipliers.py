three=[]
five=[]
for _ in range(10):
    n=int(input())
    if n%3==0:
        three.append(n)
    
    if n%5==0:
        five.append(n)
print(len(three),len(five))


    