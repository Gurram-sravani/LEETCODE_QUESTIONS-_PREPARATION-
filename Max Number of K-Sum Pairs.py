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
