import sys

def delete_space_join(str):
        return ''.join(str.lower().split())

def remove_word(name, candidate):
    return "osake"

def process_choice_pure(target_name, choice_name):
    print("本当はアナグラム", target_name, "から", choice_name, "を探す")
    return target_name

def process_choice(name):
    while True:
        choice = input('\n単語入れてね。エンターしたら終了。# でも終了:')
        if choice == '':
            sys.exit()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
            
        choice = candidate;
        result = process_choice_pure(name, choice)
        return result

if __name__ == '__main__':
    name = sys.argv[1]
    choice_name = sys.argv[2]

    # phrase = process_choice_pure(name, choice_name)
    # print("process_choice, name:", phrase)

    print('ターゲットは', name)
    result = delete_space_join(name)
    print('結果', result)
