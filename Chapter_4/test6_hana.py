def func4(start, delta, n, lst):
    # 暗号解読のためのヒントの文字列の一列目のみをつくろう
    # start = 始まりの地点、delta = 増分、n = 回数
    my_end = start + delta * n
    for i in range(start, my_end, delta):
        #print(i)
        lst.append(i)

def sign(x):
    # マイナスか、プラスか、ゼロかを判定
    if x < 0 :
        return -1
    elif x > 0:
        return 1
    else:
        return 0

# print(sign(5))

def func_x(x, lst):
    # print(abs(x), sign(x) * 4, 5)
    p0 = abs(x)
    p1 = sign(x) * 4
    p2 = 5
    print(p0, p1, p2)
    func4(p0, p1, p2, lst)

def func5(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    elif x == 3:
        return 2
    elif x == 4:
        return 3
    elif x == -1:
        return -16
    elif x == -2:
        return -17
    elif x == -3:
        return -18
    elif x == -4:
        return -19


new_lst = []

p2 = [-16, 1, -18, 3]

for e in p2:
    func_x(e, new_lst)

a0 = func5(3)
print(a0)