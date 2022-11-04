from collections import Counter

def old_counter_to_string(my_map):
    s = ''
    for letter in my_map:
        s += letter
    return s

def counter_to_string(my_map):
    my_str = ''
    for letter in my_map:
#       print("letter:",letter, "my_map[letter]:", my_map[letter])
        for i in range(my_map[letter]):
            my_str += letter
    return my_str

def include_anagram(name_map, word_map):
    for letter in word_map:
        if name_map[letter] < word_map[letter]:
            return False

    return True

def find_anagrams(name, word_list):
    for word in word_list:
#        print(word)

        name_letter_map = Counter(name)
        word_letter_map = Counter(word.lower()) # 小文字にする

        result = include_anagram(name_letter_map, word_letter_map)
        if result:
            #print('hit! ', word)
            print(word)

def process_choice(name):
    print("戻り値は本当はアナグラム", name)
    return name

if __name__ == '__main__':
    # ここから先は my_utils が実行されたとき
    #   は呼ばれるが
    # 他から import されたときは呼ばれない

    # phrase = process_choice(name)
    # print("run under my_utils, name", phrase)

    # アナグラム（複数）を表示
    name = 'tomosakarie'
    word_list = ['morita', 'sakamotoeri', 'anna', 'hana']
    find_anagrams(name, word_list)

    # map_name = Counter('sakamotoeri')
    # map_from_wordlist = Counter('tamori')
    # result = include_anagram(map_name, map_from_wordlist)
    # print(result)

    #sakamoto = Counter('sakamotoeri')
    #tamori = Counter('tamori')
    #for letter in tamori:
    #    print(letter, sakamoto[letter], tamori[letter], 
    #        1 <= sakamoto[letter], 
    #        tamori[letter] <= sakamoto[letter])

