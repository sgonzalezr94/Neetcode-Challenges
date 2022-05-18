from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = dict()
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = True
            else:
                return num
