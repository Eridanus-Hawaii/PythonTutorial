p = [(16, -4, 5), (1, 4, 5), (18, -4, 5), (3, 4, 5)]

def func_para(para, lst):
    # 暗号解読のためのヒントの文字列全部をつくろう
    for e in para:
        print(e)
        (p0, p1, p2) = e
        print("result", p0, p1, p2)

func_para(p, None)