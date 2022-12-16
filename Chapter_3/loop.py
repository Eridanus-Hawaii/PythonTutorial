from collections import Counter

name = 'yamada'
print(name)

name_map = Counter(name)
print(name_map)
print('---------------')

str=''
for letter in name_map:
    n = name_map[letter]

    for i in range(n):
        #print(letter)
        str += letter

    #print('----')

print('---------------')
print(str)
