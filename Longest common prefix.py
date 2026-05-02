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


# VERTICAL SCANNING 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == "":
            return ""
        ch = strs[0]
        for i in range(1,len(strs)):
            new_str=""
            for j in range(0,min(len(ch),len(strs[i]))):
                if ch[j]!=strs[i][j]:
                    break
                new_str+=ch[j]
                print(new_str)
            ch=new_str
            if not ch:  
                return "" 
        return ch
# TC : O(n) n is len(strs) * O(m) m is min len of comparisions (second for loop)=> O(n*m) BUT IN STRICT PYTHON IT IS o(N*M²) => O(m) for creating new_str
# sC : O(m)
