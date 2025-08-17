# 14. Longest Common Prefix


def longestCommonPrefix(strs):
    min_length = 201
    result = ""
    
    for i in strs:
        l = len(i)
        if l < min_length:
            min_length = l

    
    for i in range(min_length):
        for s in strs[1:]:
            if strs[0][i] == s[i]:
                continue
            else:
                return result 
        else:
            result += strs[0][i]
        

    return result

print(longestCommonPrefix(["flower","flow","flight"]))