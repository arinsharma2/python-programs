list = ['a', 'e', 'i', 'o', 'u']
str = "jecrccollege"
count = 0
for i in str:
    if i not in list:
        count +=1
print(count)