def printdict(dct):
    L = []
    for key, value in dct.items():
        if type(value) == type(L):
            print(key, ' -> ', ', '.join(value))
        else:
            print(key, ' -> ', value)

a = {}
key = "somekey"
a.setdefault(key, [])
a[key].append("1")

printdict(a)

a[key].append("2")


doc = {
    "TTC" : "a",
    "ATC" : "b"
}
printdict(doc)
