def find2vSumForTarget(t, l1):
    for i in l1:
        l2 = l1[l1.index(i) + 1:]
        if t - i in l2:
            return [l1.index(i), l1.index(i) + 1 + l2.index(t-i)]

    return []


def find2vSumForTarget2(t, l1):
    d1 = {}
    for i, v in enumerate(l1):
        n = t - v
        if n in d1:
            return [d1[n], i]
        d1[v]=i
    return []

print(find2vSumForTarget2(6, [3, 1, 3])) 
    
