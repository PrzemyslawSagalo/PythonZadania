class RandomQueue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def insert(self, item):
        if self.is_full():
            raise ValueError
        else:
            self.items[self.tail] = item
            self.tail = (self.tail + 1) % self.n

    def remove(self): pass   # zwraca losowy element
