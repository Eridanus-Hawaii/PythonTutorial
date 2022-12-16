<<<<<<< HEAD
# Ryo-san's code 

from collections import Counter

name = 'yamada'
=======
from collections import Counter

name = "yamada"
>>>>>>> 8bddba0f3936dbf20299fac9f2a1290ccdef59c3
print(name)

name_map = Counter(name)
print(name_map)
<<<<<<< HEAD
print('---------------')

str=''
=======
print('------------------')

str = ''
>>>>>>> 8bddba0f3936dbf20299fac9f2a1290ccdef59c3
for letter in name_map:
    n = name_map[letter]

    for i in range(n):
<<<<<<< HEAD
        #print(letter)
        str += letter

    #print('----')

print('---------------')
=======
        print(letter)
        str += letter

    print('---')

print('------------------')
>>>>>>> 8bddba0f3936dbf20299fac9f2a1290ccdef59c3
print(str)
