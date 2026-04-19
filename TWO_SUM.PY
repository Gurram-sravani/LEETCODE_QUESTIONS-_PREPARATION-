# ONE PASS - You use a single loop to iterate through the array. At each step, you check whether the complement (target - nums[i]) already exists in the hash map. If it does, you return the stored index; otherwise, you store the current number with its index in the hash map.
# TWO PASS - You use two separate loops:
First loop: build a hash map by storing each number as a key and its index as the value.
Second loop: iterate through the array again and check whether the complement (target - nums[i]) exists in the hash map.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map={}
        for i in range(len(nums)):
            x=target-nums[i]
            if x in hash_map:
                return [i,hash_map[x]]
            hash_map[nums[i]]=i
# Time Complexity : O(n)
# Space Complexity: O(n) -> Hashmap
