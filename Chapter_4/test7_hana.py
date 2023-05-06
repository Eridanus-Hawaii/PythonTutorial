width = 4
height = 5

def sign(x):
    # マイナスか、プラスか、ゼロかを判定
    if x < 0 :
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def to_start_pos(x):
    column_no = abs(x)
    # 2なら2, -3なら3
    if x > 0:
        return column_no - 1
    elif x < 0:
        pos_offset = (width * (height -1)) - 1
        return column_no + pos_offset
    
def to_delta(x):
    dir = sign(x)
    #dirは「方向」　プラス方向なら1, マイナス方向なら-1
    return dir * width

def to_repeat_n(x):
    return height
    
if __name__ =='__main__':
    rv = to_start_pos(-1)
    print(rv)