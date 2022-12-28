import sys
from my_utils import process_choice

if __name__ == '__main__':
    target_name = sys.argv[1]

    print('ターゲットは', target_name)
    result = process_choice(target_name)
    print('結果', result)
