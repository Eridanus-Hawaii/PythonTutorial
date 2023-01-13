import sys
from phrase_anagrams import process_choice

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage:test03.py 名前')
        print('名前の設定が必要だよ')
        sys.exit(1)

    if len(sys.argv) >= 3:
        print('Usage:test03.py 名前')
        print('おおすぎだよ')
        sys.exit(1)

    name = sys.argv[1]

    print("Start name:", name)
    result = process_choice(name)
    print("result:", result)
