text = ['REST', 'TRANSPORT', 'YOU', 'GODWIN', 'VILLAGE', 'ROANOKE', 'WITH', 'ARE', 'YOUR', 'IS', 'JUST', 'SUPPLIES', 'FREE', 'SNOW', 'HEADING', 'TO', 'GONE', 'TO', 'SOUTH', 'FILLER']

honto_text = [None] * 20
order = [16, 12, 8, 4, 0, 1, 5, 9, 13, 17, 18, 14, 10, 6, 2, 3, 7, 11, 15, 19]

def my_view(lst):
    i = 0
    for ii in range(5):
        for jj in range(4):
            print(f'{lst[i]} ', end=' ')
            i += 1
        print()

for i, e in enumerate(order):
    honto_text[e] = text[i]
    my_view(honto_text)
    print("============")

print(honto_text)