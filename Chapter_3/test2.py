import sys
from phrase_anagrams import process_choice

if __name__ == '__main__':
    name = sys.argv[1]

    print("Start name:", name)
    result = process_choice(name)
    print("result:", result)
