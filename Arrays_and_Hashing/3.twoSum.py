from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = dict()
        for idx, num in enumerate(nums):
            if target - num not in idx_dict:
                idx_dict[num] = idx
            else:
                return [idx_dict[target - num], idx]
