import time



honto_text = [None]*20
cypher_text = ['REST', 'TRANSPORT', 'YOU', 'GODWIN', 'VILLAGE', 'ROANOKE', 'WITH', 'ARE', 
'YOUR', 'IS', 'JUST', 'SUPPLIES', 'FREE', 'SNOW', 'HEADING', 'TO', 'GONE', 'TO', 'SOUTH', 'FILLER']
order = [16, 12, 8, 4, 0, 1, 5, 9, 13, 17, 18, 14, 10, 6, 2, 3, 7, 11, 15, 19]

def my_view(lst):
    # create 4x5 box to make easy to read 
    i = 0
    for ii in range(5):
        for jj in range(4):
            print(f'{lst[i]} ', end=' ')
            i += 1
        print()

for i, e  in enumerate(order):
    print(f'{e} に暗号分の{i}番目の文言{cypher_text[i]}を入れる')
    honto_text[e] = cypher_text[i]
    my_view(honto_text)
    print("================")
    
def my_init():
    # initialize list 
    honto_text = []
    for i in range(20):
        honto_text.append(i)
    return honto_text