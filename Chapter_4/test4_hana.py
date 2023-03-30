def sign(x):
    # マイナスか、プラスか、ゼロかを判定
    if x < 0 :
        return -1
    elif x > 0:
        return 1
    else:
        return 0

# print(sign(5))

def func_x(x):
    print(abs(x), sign(x) * 4, 5)
    # 暗号解読のためのヒントの文字列全部をつくろう をもっと簡単にした

p2 = [-16, 1, -18, 3]

for e in p2:
    func_x(e)