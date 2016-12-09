def solve1(a, b, c):
    """Rozwiazywanie rownania liniowego a x + b y + c = 0."""
    if b == 0:
        raise ValueError('b nie moze byc rowne 0')
    else:
        if a == 0 and c == 0:
            to_return = 'y=0'
        elif a == 0:
            to_return = 'y={}'.format(-c / float(b))
        elif c == 0:
            to_return = 'y={}*x'.format(-a/float(b))
        else:
            to_return = 'y={0}*x{1}'.format(-a/float(b), -c/float(b))

    return to_return
