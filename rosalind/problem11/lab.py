def interpol(setlist):
    for i in range(len(setlist)):
        set1 = setlist[0]
        set1.intersection_update(setlist[i])
    return set1

def factorial(x):
    i = 1
    ret = 0
    while i <= x:
        ret += i
        i+=1
    return ret

a = {"ATA","AAA"}
a = {'TAT', 'GGT', 'TGT', 'CTT', 'AGC', 'TTT', 'AGG', 'TCG', 'ACT', 'GTC', 'GGA', 'TCT', 'TGG', 'TTG', 'ATA', 'GAC', 'ATC', 'ATG', 'GCC', 'GGG', 'TGC', 'AGT', 'AAT', 'GTT', 'TTC', 'CTG', 'GTG', 'TGA', 'GGC', 'CGG', 'TTA', 'ATT', 'TAG', 'CGC'}
b = {"AAA",}
b = {'CCT', 'TGT', 'CTT', 'AGC', 'CTA', 'TTT', 'GCA', 'TAA', 'CTC', 'ACT', 'CCC', 'GTC', 'TCC', 'TCT', 'TGG', 'TAC', 'GCT', 'ATA', 'GAC', 'CGT', 'TTG', 'GCC', 'GCG', 'TGC', 'GTT', 'TTC', 'CTG', 'TGA', 'GGC', 'CCG', 'TTA', 'ATT', 'ACC', 'CCA', 'CAT', 'GTA', 'CGC', 'TCA'}
c = {"CCC","TEG","ATA"}
c = {'GAT', 'TAT', 'CAG', 'GGT', 'TGT', 'AGC', 'CGA', 'CTA', 'GCA', 'TAA', 'TTT', 'CTC', 'AGG', 'GTC', 'GGA', 'TCT', 'TGG', 'TAC', 'GCT', 'ATA', 'CGT', 'ATC', 'ATG', 'GGG', 'AGT', 'AAT', 'GTT', 'TTC', 'CTG', 'GTG', 'GGC', 'CGG', 'CCG', 'TTA', 'ATT', 'ACC', 'GAA', 'TAG', 'CAT', 'GTA', 'CGC', 'AAC'}
d = {"ABC","ATA"}
d = {'GAT', 'TAT', 'CTT', 'GAG', 'AAG', 'AAA', 'TTT', 'GCA', 'TAA', 'ACT', 'CAA', 'GGA', 'ATA', 'GAC', 'ATC', 'ATG', 'AGT', 'AGA', 'AAT', 'GTT', 'ACA', 'ATT', 'GAA', 'CAT', 'GTA', 'AAC'}
sli = [a,b,c,d]

print(interpol(sli))

