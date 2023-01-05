def longestCommonPrefix(self,strs):
    count = len(strs)
    if count ==1:
        return strs[0]
    else:
        return strs