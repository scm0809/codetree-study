num1,num2=map(int,input().split())
num_list=[num1,num2]
for i in range(8):
    sum_list1= num_list[i]
    sum_list2= num_list[i+1]
    sum_list= sum_list1 + sum_list2
    one= sum_list % 10
    num_list.append(one)
print(*num_list,end='')