import sys
from process_choice_anna import remove_word

if __name__ == '__main__':
    name = sys.argv[1]
    choice_name = sys.argv[2]

    phrase = remove_word(name, choice_name)
    print("remove_word:",name, choice_name, " ----> ", phrase)