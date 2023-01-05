class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0;
        max =1;
        for i in range(0,len(s)):
            if max > len(s)-i or max>=128:
                return max
            arr = [None for i in range(128)] 
            count=1;
            arr[ord(s[i])]=s[i]
            for j in range(i+1, len(s)):    
                if s[j] ==arr[ord(s[j])]:
                    break;
                arr[ord(s[j])]=s[j]
                count+=1;
                if count > max:
                    max=count;
        return max;
        """
        :type s: str
        :rtype: int
        """
string1='abcabcbb'
string2='pwwkew'
string3="aab"
string4='dvdf'
string5='bbbb'
x = Solution()
print(x.lengthOfLongestSubstring(string1));
print(x.lengthOfLongestSubstring(string2));
print(x.lengthOfLongestSubstring(string3));
print(x.lengthOfLongestSubstring(string4));
print(x.lengthOfLongestSubstring(string5));