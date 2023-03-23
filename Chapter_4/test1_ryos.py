cypher_text = ['REST', 'TRANSPORT', 'YOU', 'GODWIN', 'VILLAGE', 'ROANOKE', 'WITH', 'ARE', 'YOUR', 'IS', 'JUST', 'SUPPLIES', 'FREE', 'SNOW', 'HEADING', 'TO', 'GONE', 'TO', 'SOUTH', 'FILLER']

honto_text = []
for i in range(20):
    honto_text.append(i)

order = [16, 12, 8, 4, 0, 1, 5, 9, 13, 17, 18, 14, 10, 6, 2, 3, 7, 11, 15, 19]

def my_view(lst):
    i = 0
    for ii in range(5):
        for jj in range(4):
            print(f'{lst[i]} ', end=' ')
            i += 1
        print()

import time

for i, e  in enumerate(order):
    honto_text[e] = cypher_text[i]
    my_view(honto_text)
    print("============")
    time.sleep(1)

print(honto_text)

"""
0    1    2     3
4    5    6     7
8    9   10    11
12  13   14    15
16  17   18    19
"""

def func4(start, span, n):
    x = start
    for i in range(n):
        print(x)
        x += span

