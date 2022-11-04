import sys
from collections import Counter
from my_utils import include_anagram, counter_to_string

if __name__ == '__main__':
    target_name = sys.argv[1]
    dic_word = sys.argv[2]

    target_name_map = Counter(target_name)
    dic_word_map = Counter(dic_word)

    result = include_anagram(target_name_map, dic_word_map)
    if result:
        remain_map = target_name_map - dic_word_map
        remain = counter_to_string(remain_map)
        remain_tuple = (dic_word, remain)
        print("Test name:", target_name, dic_word, "=>", result, remain_tuple)
    else:
        print("Test name:", target_name, dic_word, "=> False!!!!!!!!!!!!")

