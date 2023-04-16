class Cipher:
    def __init__(self, width = 4, height = 5):
        self.width = width
        self.height = height
        self.keys = None

    def sign(self, x):
        if x < 0:
            return -1
        elif x > 0:
            return 1
        else:
            return 0

    def start_pos(self, column):
        if column > 0:
            return column - 1
        elif column < 0:
            return -column + (self.width * (self.height - 1)) - 1

        # error!!

    def add_sequence(self, lst, pos, delta, repeat_n):
        num = pos
        for i in range(repeat_n):        
            lst.append(num)
            num += delta
        
    def make_sequence(self, keys):
        lst = []
        for column in keys:
            pos = self.start_pos(column)
            delta = self.sign(column) * self.width
            repeat_n = self.height

            self.add_sequence(lst, pos, delta, repeat_n)
        return lst

    def set_keys(self, keys):
        self.keys = keys

    def decode(self, string_lst):
        seq = self.make_sequence(self.keys)
        result = [None] * (self.width * self.height)
        for i, word in enumerate(string_lst):
            num = seq[i]
            result[num] = word
        return result
            
if __name__ == '__main__':
    cipher = Cipher()
    lst = cipher.make_sequence([-1, 2, -3, 4])
    print(lst)

    cipher.set_keys([-1, 2, -3, 4])
    result = cipher.decode(["REST", "TRANSPORT", "YOU", "GODWIN", "VILLAGE", "ROANOKE", "WITH", "ARE", "YOUR", "IS", "JUST", "SUPPLIES", "FREE", "SHOW", "HEADING", "TO", "GONE", "TO", "SOUTH", "FILLER"])
    print(result)
