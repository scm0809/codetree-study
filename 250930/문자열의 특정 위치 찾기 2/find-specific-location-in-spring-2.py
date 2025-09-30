w=["apple", "banana","grape","blueberry","orange"]
found=[]
A=input()
for word in w:
    third=(word[2]==A)
    forth=(word[3]==A)
    if third or forth :
        found.append(word)
for i in found:
    print(i)
print(len(found))
    

