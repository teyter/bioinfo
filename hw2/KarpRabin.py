def hass(s):
    a = {
        "A" : 0,
        "C" : 1,
        "G" : 2,
        "T" : 3
        }
    d = 4
    f = len(s)-1
    ret = 0
    q = 64
    for i in range(len(s)):
        ret+= d**f * a[s[i]]
        f-=1
    return ret % q

def KP(P,T):
    p = hass(P)
    m = len(T)
    n = len(P)
    for i in range(m-n+1):
        if hass(T[i:i+n]) == p:
            print(i)
            if T[i:i+n] == P:
                print(i)
                return i
    return -1

s = "AAAACAAAGAAATTT"
p = "GAAA"
KP(p,s)
