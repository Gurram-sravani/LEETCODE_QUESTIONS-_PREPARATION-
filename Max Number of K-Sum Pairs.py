class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash_map={}
        cnt=0
        for i in range(len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        for n in nums:
            current=n
            complement=k-n
            if hash_map.get(current, 0) > 0 and hash_map.get(complement, 0) > 0:
                if current==complement and hash_map[current]<2: 
                    continue
                else:
                    hash_map[current]-=1
                    hash_map[complement]-=1
                cnt+=1
        return cnt
# Time Complexity: O(n) creating Hash_map + O(n) checking n in nums
# Space Complexity : O(n) hash_map 
-- This is two pass solution - we are doing extra work here - see and understand example below.
nums=[1,1,1,1]
for n in nums:
Iteration 1: current=1,complement=1 => (1,1) so the count becomes 2 in hashmap
Iteration 2: current=1,complement=1 => (1,1) so the count becomes 0 in hashmap 
Iteration 3: loops through the third element 
Iteration 4: loops through 4th element
Half your loop is useless....
