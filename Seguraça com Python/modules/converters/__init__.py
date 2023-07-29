def binConverter(n, f=False):
    '''
    -> binary to decimal converter
    :param n: binary number
    :param f: formatted result
    :return: decimal result
    '''
    n = str(n)
    binAux = []
    s = 0
    m = 2
    for p, c in enumerate(n):
        binAux.append(p)
    binAux.sort(reverse=True)
    for p, c in enumerate(binAux):
        if p + 1 == 1 and n[c] == '1':
            s += 1
        elif p + 1 == 2 and n[c] == '1':
            s += 2
        elif p + 1 > 2:
            m *= 2
            if n[c] == '1':
                s += m
    return s if f is False else f'''Binary: {n}
Decimal: {s}'''


def octalConverter(n, f=False):
    '''
    -> octal to decimal converter
    :param n: octal number
    :param f: formatted result
    :return: decimal result
    '''
    n = str(n)
    oct = 0
    octAux = []
    for p, c in enumerate(n):
        octAux.append(p)
    octAux.sort(reverse=True)
    for p, c in enumerate(octAux):
        aux = int(n[c])
        mem = aux * (8 ** p)
        oct += mem
    return oct if f is False else f'''Octal: {n}
Decimal: {oct}'''
