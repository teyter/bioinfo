def bw():
    s = "GATTACAATTAC$"
    bla = len(s)
    s *=100
    for i in range(len(s)-1,-1,-1):
        print(s[i-bla:i])

def printlist(li):
    for i in li:
        print(i)

ss = [
"GATTACAATTAC$",
"$GATTACAATTAC",
"C$GATTACAATTA",
"AC$GATTACAATT",
"TAC$GATTACAAT",
"TTAC$GATTACAA",
"ATTAC$GATTACA",
"AATTAC$GATTAC",
"CAATTAC$GATTA",
"ACAATTAC$GATT",
"TACAATTAC$GAT",
"TTACAATTAC$GA",
"ATTACAATTAC$G"
]
ss.sort()
printlist(ss)
