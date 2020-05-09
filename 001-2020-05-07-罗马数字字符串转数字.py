def romaStrToNum(s) -> int:
    result = 0
    d1 = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM': 900, 'M':1000} 
    c = 0
    while c < len(s):
        s1 = s[c]
        s2 = ''
        if len(s) > (c+1):
            s2 = s[c+1]

        s3 = s1+s2

        v1 = d1[s1]
        v2 = 0
        if len(s2):
            v2 = d1[s2]

        if s3 in d1:
            result += d1[s3]
            c += 2
        else:
            result += v1
            c += 1

    return result

print(romaStrToNum('CCLXXI'))   #271
print(romaStrToNum('CCLXX'))    #270
print(romaStrToNum('CDXC'))     #490
print(romaStrToNum('MCMXCIV'))  #1990