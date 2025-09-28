a=input()
n=len(a)
a_list=list(a)
a_list[1]='a'
a_list[n-2]='a'
a_sen="".join(a_list)
print(a_sen)