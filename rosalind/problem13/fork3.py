import numpy as np
from teitlib import *

def matrix2string(matrix):
    acgt = "ACGT"
    maxx = 0
    index = 0
    for i in range(len(matrix)):
        vector = matrix[i]
        for j in range(4):
            maxx = max(vector)
            index = np.where(vector == maxx)
            print(maxx)
    return 0

def letter(vector):
    dic = {
       vector[0] : "A",
       vector[1] : "C",
       vector[2] : "G",
       vector[3] : "T"
    }
    ret = dic[max(vector)]
    vector[np.where(vector == max(vector))] -= 0.1
    return ret

def kmer(matrix):
    string = ""
    likely = []
    while isMatrixNull(matrix):
        print(matrix)
        print()
        string = ""
        for i in range(len(matrix)):
            string += letter(matrix[i])
        likely.append(string)
    return likely

def isMatrixNull(matrix):
    for i in range((len(matrix))):
        for j in range(4):
            x = matrix[i][j]
            if x > -0.1:
                return True
    return False

def Xprofile(matrix):
    dic = {
       matrix[0] : "A",
       matrix[1] : "C",
       matrix[2] : "G",
       matrix[3] : "T"
    }
    string = ""
    likely = []
    while isMatrixNull(matrix):
        for i in range(len(matrix)):
            string += dic[max(matrix[i])]
            matrix[np.where(matrix == max(matrix[i]))] -= 0.1
        likely.append(string)
    return likely

def debug():
    # debug test
    matrix = np.loadtxt('debug_matrix.txt').T
    text = "AGCAGCTTTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATCTGAACTGGTTACCTGCCGTGAGTAAAT"
    print(kmer(matrix))

debug()
