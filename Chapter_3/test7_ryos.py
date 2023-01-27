import sys
from process_choice_ryos import process_choice_pure

if __name__ == '__main__':
    name = sys.argv[1]
    choice_name = sys.argv[2]

    phrase = process_choice_pure(name, choice_name)
    print("process_choice, name:", phrase)
