# Python 2.7.4.
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

print 'cala lista'
print_list(head)

# ------------------------------------------------------------------------------
def remove_head(node):
    if node == None:
        raise ValueError
    else:
        new_head = node.next
        data = node.data

    return new_head, data

# Sprawdzenie
head, data = remove_head(head)
print "lista po usunieciu pierwszego elementu"
print_list(head)


def remove_tail(node):
    if node == None:
        raise ValueError
    elif node.next == None:
        return None, node.data
    else:
        head = node
        while node:
            last = node
            if last.next.next == None:
                data = last.next.data
                last.next = None
                return head, data
            else:
                node = node.next

# Sprawdzenie
head, data = remove_tail(head)
print "lista po usunieciu ostatniego elementu"
print_list(head)