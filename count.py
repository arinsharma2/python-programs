# str = "cse 048"
# letter = 0
# num = 0
# space = 0
# for char in str:
#     if char.isalpha():
#         letter += 1
#     elif char.isdigit():
#         num += 1
#     elif char ==" ":
#         space += 1
# print("no of letters", letter)
# print("no of digits: ", num)
# print("no of spaces: ", space)

# import re
# name = 'Python is 1'
# digitCount = re.sub("[^0-9]", "", name)
# letterCount = re.sub("[^a-zA-Z]", "", name)
# spaceCount = re.findall("[ \n]", name)
# print(len(digitCount))
# print(len(letterCount))
# print(len(spaceCount))

def analyse_string(text : str):
    digitCount = sum(c.isalpha() for c in text)
    letterCount = sum(c.isdigit() for c in text)
    spaceCount = sum(c.isspace() for c in text)
    specialCount = [c for c in text if not(c.isalpha() or c.isdigit() or c.isspace())]

    return {
        "Digits" : digitCount,
        "Letter" : letterCount, 
        "Space" : spaceCount,
        "Special" : len(specialCount),
        "Special Characters" : specialCount
    }

name = "Python is 1@%"
result = analyse_string(name)

for key, value in result.items():
    print(f"{key} : {value}")