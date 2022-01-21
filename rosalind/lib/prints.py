def oneline(lst):
    print(' '.join(map(str,lst)))

def printlst(lst):
    for i in lst: print(i)

def printdict(dct):
    for key, value in dct.items():
        print(key, '->', ','.join(value))

def path_output(lst):
    print( '->'.join(map(str,lst)))
