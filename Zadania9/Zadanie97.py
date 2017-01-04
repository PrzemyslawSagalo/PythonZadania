class Node:
    """Klasa reprezentujaca wezel drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

# Reczne budowanie wiekszego drzewa.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def count_leafs(top):
    liczba_lisci = 0
    # Funkcja wewnetrzna do sprawdzania czy na obu galeziach sa potomkowie.
    def count(item):
        if item.left == None and item.right == None:
            return 1
        else:
            return 0

    if top is None:
        return 0
    liczba_lisci += count(top)
    liczba_lisci += count_leafs(top.left)
    liczba_lisci += count_leafs(top.right)

    return liczba_lisci

print count_leafs(root)