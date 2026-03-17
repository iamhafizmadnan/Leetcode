class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        hashmap = {}

        for i , num in enumerate(sorted_nums):
            if num not in hashmap:
                hashmap[num] = i
        
        return [hashmap[num] for num in nums]


# Sorting → O(n log n)
# HashMap → O(n)
# Final → O(n)
#  Final = O(n log n)

