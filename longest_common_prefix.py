def longestCommonPrefix(strs):
    rstring = strs[0]
    if len(strs) ==1:
        return strs[0]
    else:
        for i in range(1,len(strs)):
            count = 0
            word = strs[i]
            for char in rstring:
                if count >= len(word):
                    rstring =word
                    break
                if char == word[count]:
                    count+=1
                else:
                    if count ==0:
                        return('')
                    newstring=rstring[0:count]
                    rstring = newstring
    return rstring



strs = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
print(longestCommonPrefix(strs))
print(longestCommonPrefix(strs2))
strs3=["aaa","aa","aaa"]
print(longestCommonPrefix(strs3))
