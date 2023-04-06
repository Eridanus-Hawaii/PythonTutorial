p = [(16, -4, 5), (1, 4, 5), (18, -4, 5), (3, 4, 5)]
def func4(start, delta, n, lst):
    my_end = start + delta * n
    for  i in range(start, my_end, delta):
        # print(i)
        lst.append(i)

def func_para(para, lst):
    for e in para:
        print(e)
        (p0, p1, p2) = e
        print('result:', p0, p1, p2)
        func4(p0, p1, p2, lst)

new_lst = []
func_para(p, new_lst)

def sign(x):
    if x < 0:
        return -1 
    elif x > 0:
        return 1 
    else:
        return 0 
    
def func_x(x, lst):
    print(abs(x), sign(x) * 4, 5)
    p0 = abs(x)
    p1 = sign(x) * 4
    p2 = 5
    func4(p0, p1, p2, lst)

p2 =  [-16, 1, -18, 3]
for e in p2:
    func_x(e, new_lst)


def f(x):
    if x > 0:
        return x-1
    else:
        return x-15
    
for e in (-1, 2, -3, 4):
    print(f(e))

for e in (-1, 2, -3, 4):
    func_x(f(e), new_lst)


def ff(lst):
    new_lst = [] 
    for e in lst:
        func_x(f(e), new_lst)
    return new_lst


# updated 4/5