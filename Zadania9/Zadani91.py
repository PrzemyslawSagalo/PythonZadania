class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

head = None
# pusta lista

head = None                   # [], pusta lista
head = Node(3, head)          # [3]
head = Node(2, head)          # [2, 3]
head = Node(4, head)          # [4, 2, 3]

def print_list(node):
    """Iteracyjne wypisanie listy jednokierunkowej."""
    while node:
        print node
        node = node.next

def remove_head(node):
    # Funkcje powinny zwracac pare(new_head, data)
    '''
    Funkcja zwraca:
    new_head - instancja Node ktora do momentu usuniecia pierwszego elementu byla drugim elementm
    data - wartosc ktora byla przypisana do pierwszego elementu, ktory zostal usuniety.
    '''
    if node == None:
        raise ValueError
    else:
        new_head = node.next
        data = node.data

    return new_head, data

def remove_tail(node):
    if node == None:
        raise ValueError
    else:
        while node:
            next_node = node.next
            if next_node == None:
                node.next = None
                return next_node, node.data
            elif next_node.next == None:
                node.next = None
                return next_node, node.data
            else:
                node = next_node

# remove_tail(head)

print_list(head)

