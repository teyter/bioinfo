def Pr(Pattern,Profile):
    A = Profile[0]
    C = Profile[1]
    G = Profile[2]
    T = Profile[3]
    pr = 1.0
    for i in range(len(Pattern)):
        if Pattern[i] == "A":
            pr *= A[i] + 1
        if Pattern[i] == "C":
            pr *= C[i] + 1
        if Pattern[i] == "G":
            pr *= G[i] + 1
        if Pattern[i] == "T":
            pr *= T[i] + 1
    return pr
