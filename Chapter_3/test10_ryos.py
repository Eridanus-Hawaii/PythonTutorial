import sys
from process_choice_anna import remove_word, delete_space_join

if __name__ == '__main__':
    name = sys.argv[1]
    choice_name = sys.argv[2]

    name = delete_space_join(name)
    candidate = delete_space_join(choice_name)
    phrase = remove_word(name, candidate)
    print("remove_word:",name, choice_name, " ----> ", phrase)
