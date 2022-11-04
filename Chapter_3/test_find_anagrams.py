import sys
import load_dictionary
import phrase_anagrams
import my_utils

# python3 test_find_anagrams.py phrase_anagrams tomosakarie 2of4brif.txt
# python3 test_find_anagrams.py my_utils tomosakarie 2of4brif.txt
if __name__ == '__main__':
    which_function = sys.argv[1]
    name           = sys.argv[2]
    dict_file      = sys.argv[3]

    word_list = load_dictionary.load(dict_file)

    if which_function == 'phrase_anagrams':
        phrase_anagrams.find_anagrams(name, word_list)
    elif which_function == 'my_utils':
        my_utils.find_anagrams(name, word_list)
    else:
        print("わかりません")
