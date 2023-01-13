import sys
from my_utils import ignore_space_join

if __name__ == '__main__':
    target_name = sys.argv[1]

    #print('ターゲットは', target_name)
    print(f'ターゲットは"{target_name}"')
    result = ignore_space_join(target_name)
    print('結果', result)
