from my_utils import process_choice, find_anagrams

def my_process_choice(name):
    print('process_choice:', name)

    return 'Yamada Taro'

def main(name):
    print('main:', name)

    name = ''.join(name.lower().split())
    name = name.replace('-', '')

    phrase =''
    limit = 17
    limit = len(name)
    running = True

    # カウンターをゼロで初期化
    counter = 0

    print('    はじまり:', counter)

    word_list = []

    while running:
        counter += 1
        print('    while: running:', running, 'counter:', counter)

        temp_phrase = phrase.replace(' ', '')

        print('       len temp_phrase:', len(temp_phrase), ' limit:', limit)
        if len(temp_phrase) < limit:
            print('        処理中', name)

            find_anagrams(name, word_list)

            phrase=process_choice(name)
            print('phrase', phrase)

            #phrase=name

        elif len(temp_phrase) == limit:
            print('        終了処理')
            break

##

if __name__ == '__main__':
    ini_name = input('Please Input Your Name:')
    print(ini_name)

    main(ini_name)
