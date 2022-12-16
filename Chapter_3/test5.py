import sys
from collections import Counter
from my_utils import counter_to_string

if __name__ == '__main__':
    target_name = sys.argv[1]

    target_name_map = Counter(target_name)

    result = counter_to_string(target_name_map)
    print(target_name_map, " => ", result)
