s = "(())()"

class Dict:
    def __init__(self):
        self.items = [None] * 2

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]

def is_correct_parenthesis(string):
    # 구현해보세요!
    # key/value = [('(',1),(')',-1]
    # for s, if sum of string >= 0: True, else: False

    parent_dict = Dict()
    parent_dict.put('(', 1)
    parent_dict.put(')', -1)

    std_parent = 0
    for p in string:
        std_parent += parent_dict.get(p)
        if std_parent >= 0:
            continue
        else:
            return False

    return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!