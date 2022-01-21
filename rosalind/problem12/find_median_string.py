import sys

data = sys.stdin.readlines()
k = int(data[0].strip())
dna = []
for line in data[1:]:
	dna.append(line.strip())

def getMaxFromDict(d):
	maxDict = {}
	maxValue = 0

	for i in d:
		if d[i] > maxValue:
			maxDict = {}
			maxValue = d[i]
			maxDict[i] = d[i]
		elif d[i] == maxValue:
			maxDict[i] = d[i]
	return maxDict

dna_kmer = {}
for dna_item in dna:
	for dk in [dna_item[i:i+k] for i in range(len(dna_item)-(k-1))]:
		if dk not in dna_kmer:
			dna_kmer[dk] = 1
		else:
			dna_kmer[dk] += 1


#print(list(getMaxFromDict(dna_kmer))[0])
print(list(getMaxFromDict(dna_kmer)))
print(dna_kmer)
