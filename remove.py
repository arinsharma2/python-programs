# lst = ['a', 'a', 'b', 'b', 'c', 'c']
# result = set(lst)
# print(list(result))

#Remove Duplicates from a list 
def remove_duplicates(lst):
    return list(set(lst))
print(remove_duplicates([1,2,3,4,3,2,1,2]))