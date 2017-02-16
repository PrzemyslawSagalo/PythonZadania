import random

class RandomQueue:

    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):
        return False

    def insert(self, data):
        self.items.append(data)

    def remove(self):
        if self.is_empty():
            raise ValueError
        else:
            it = random.randint(0, len(self.items)-1) # losujemy element
            print it

            temp = self.items[it] # przypisujemy wylosowana wartosc to tymczasowej zmiennej

            i_last = len(self.items) - 1

            self.items[it] = self.items[i_last] # przeypisujemy ostatnia wartosc do pozycji it

            del self.items[i_last] # usuwamy ostatni element

            return temp # zwracamy wylosowana wartosc

kolej1 = RandomQueue()

for i in range(3):
    kolej1.insert(i)

kolej1.remove()
print kolej1
kolej1.remove()
print kolej1
kolej1.remove()
print kolej1


