from random import randrange


class RandomizedSet:

    def __init__(self):
        self.hashmap = set()
        self.keys = list()
        self.key_to_val = dict()
        self.n_keys = 0

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.hashmap.add(val)  # set
            self.keys.append(val)  # list
            self.key_to_val[val] = self.n_keys  # dict
            self.n_keys += 1  # counter
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            self.hashmap.remove(val)  # set

            new_pos = self.key_to_val[val]
            self.keys[new_pos] = self.keys[-1]  # list
            new_val = self.keys[new_pos]
            self.keys.pop()

            self.key_to_val[new_val] = new_pos
            del self.key_to_val[val]  # dict

            self.n_keys -= 1  # counter
            return True
        return False

    def getRandom(self) -> int:
        return self.keys[randrange(self.n_keys)]
