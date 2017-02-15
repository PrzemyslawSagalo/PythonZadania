def solve1(a, b, c):
    """Rozwiazywanie rownania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0 and c == 0:
        to_return = 'rownanie jest zawsze spelnione'
    elif a == 0 and b == 0 and c != 0:
        to_return = 'rownanie jest sprzeczne'
    elif a == 0 and b != 0 and c == 0:
        to_return = 'y=0'
    elif a == 0 and b != 0 and c != 0:
        to_return = 'y={}'.format(-c/float(b))
    elif a != 0 and b == 0 and c == 0:
        to_return = 'x=0'
    elif a != 0 and b == 0 and c != 0:
        to_return = 'x={}'.format(-c/float(a))
    elif a != 0 and b != 0 and c == 0:
        to_return = 'y={} x'.format(-a/float(b))
    elif a != 0 and b != 0 and c != 0:
        to_return = 'y={0} x {1}'.format(-a/float(b), -c/float(b))

    return to_return
