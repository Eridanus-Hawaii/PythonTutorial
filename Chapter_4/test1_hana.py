text = ['REST', 'TRANSPORT', 'YOU', 'GODWIN', 'VILLAGE', 'ROANOKE', 'WITH', 'ARE', 'YOUR', 'IS', 'JUST', 'SUPPLIES', 'FREE', 'SNOW', 'HEADING', 'TO', 'GONE', 'TO', 'SOUTH', 'FILLER']

honto_text = [None] * 20
order = [16, 12, 8, 4, 0, 1, 5, 9, 13, 17, 18, 14, 10, 6, 2, 3, 7, 11, 15, 19]

for i, e in enumerate(order):
    honto_text[e] = text[i]

print(honto_text)