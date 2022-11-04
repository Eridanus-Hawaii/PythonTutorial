import sys
from collections import Counter
from my_utils import include_anagram

if __name__ == '__main__':
    target_name = sys.argv[1]
    dic_word = sys.argv[2]

    target_name_map = Counter(target_name)
    dic_word_map = Counter(dic_word)

    result = include_anagram(target_name_map, dic_word_map)
    print("Test name:", target_name, dic_word, "=>", result)


