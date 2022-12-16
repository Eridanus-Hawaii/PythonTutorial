import sys
from collections import Counter
from my_utils import counter_to_string

# additional practice on 12/15/22
name = 'yamada'
print(name)

name_map = Counter(name)
print(name_map)
print('----------------')


str = ''
for letter in name_map:
    n = name_map[letter] # number of each letter in Counter  

    for i in range(n):
        #print(letter)
        str += letter
    #print(n)

    print('---')

print('----------------')
print(str)