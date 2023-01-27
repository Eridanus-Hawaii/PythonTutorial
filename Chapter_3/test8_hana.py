import sys
from process_choice_hana import delete_space_join

if __name__ == '__main__':
    name = sys.argv[1]

    result = delete_space_join(name)
    print(name, '\t\t->\t', result)