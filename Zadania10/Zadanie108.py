import random

class RandomQueue:

    def __init__(self, n):
        self.size = n
        self.items = [None] * self.size
        self.i = 0

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        if self.i == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.i == self.size:
            return True
        else:
            return False

    def insert(self, data):
        if self.is_full():
            raise ValueError
        else:
            self.items[self.i] = data
            self.i += 1

    def remove(self):
        if self.is_empty():
            raise ValueError
        else:
            it = random.randint(0, self.i-1)
            print it

            data = self.items.pop(it) # wycigamy it element z koleiki

            self.items.append(None) # dopisujemy do konca kolejki None

            self.i -= 1 # cofamy o jeden iterator

            return data

kolej1 = RandomQueue(3)

for i in range(3):
    kolej1.insert(i)

kolej1.remove()
kolej1.remove()
kolej1.remove()

print kolej1