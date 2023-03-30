def func4(start, delta, n, lst):
    my_end = start + delta * n
    for i in range(start, my_end, delta):
        #print(i)
        lst.append(i)

hana_list = []

func4(16, -4, 5, hana_list)

print(hana_list)