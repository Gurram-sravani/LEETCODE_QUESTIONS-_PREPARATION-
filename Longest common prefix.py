class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == "":
            return ""
        # Horizontal Scanning - You compare the first two strings to find their common prefix, then use that result to compare against the third string, and so on.
        prefix=strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix)!=0:  # find returns 0 if the prefix found else it will return -1 
                prefix=prefix[0:len(prefix)-1]
                if prefix=="":
                    return ""
        return prefix

# tc: O(n) n is len of strs * while loop O(m) m is len of prefix * strs[i].find(prefix)!=0 O(m)  => TC: O(N * M²)
# sc : O(1) 
