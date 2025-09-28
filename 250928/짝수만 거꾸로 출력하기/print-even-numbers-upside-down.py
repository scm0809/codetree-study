N=int(input())
a=list(map(int,input().split()))
num_list=[]
for num in a:
    if num%2==0:
        num_list.append(num)
print(*num_list[::-1])