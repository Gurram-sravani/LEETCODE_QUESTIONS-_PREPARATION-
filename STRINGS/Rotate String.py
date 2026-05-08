class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        new_str=s+s   # O(2n)
        if goal in new_str:       # new_str.find(goal) != -1  ----> O(2n*n) =>O(n^2)
            return True
        else:
            return False
# Time Complexity : O(n) positions×O(n) comparisons each=O(n^2)
# space Complexity1: O(2n)

Knuth-Morris-Pratt KMP String Matching Algorithm:

