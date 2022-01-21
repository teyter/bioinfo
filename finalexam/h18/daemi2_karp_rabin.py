T = "ACGTGATGCGCATCGTACGCTCG"
N = len(T)
q = 23

def listAllK(Text,k):
    return [Text[i:i+k] for i in range(len(Text)-k+1)]

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
    q = 23
    for i in range(len(s)):
        ret+= d**f * a[s[i]]
        f-=1
    return ret % q

def fall(T,k,w):
    allK = listAllK(T[0:w],k)
    allH = [hass(i) for i in allK]
    x = min(allH)
    print(allH)

k = 3
w = int(n/2)
fall(T,k,w)

O(w-k+1) + O((w-k+1)*w) + O(w-k+1)

O(n-w+1) * ^^           
