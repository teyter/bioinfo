import numpy as np
from teitlib import *

def exer(p,q):
    p = list(p)
    q = list(q)
    ret = ""
    for i in range(len(p)):
        if p[i] == q[i]:
            ret += p[i]
        else:
            ret += q[i].lower()
    return ret

p = "AGCAGCTT"
q = "ATCAATGC"
    "AtCAatgc"

print(exer(p,q))
p = "CCGAG"
q = "CGGCG"

