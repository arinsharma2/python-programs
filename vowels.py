# list = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'I', 'U']
n = input("enter a string: ")
vow = "AEIOUaeiou"
# str = "sajbsaba"
count = 0
for i in n:
    if i in vow:
        count +=1

print(count)