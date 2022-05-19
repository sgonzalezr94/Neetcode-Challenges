from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        dict_occurences = dict()
        if len(nums) == 1:
            return nums
        while i < len(nums) / 2:
            print(i, j)
            if nums[i] not in dict_occurences:
                dict_occurences[nums[i]] = 1
            else:
                dict_occurences[nums[i]] += 1
            if nums[j] not in dict_occurences:
                dict_occurences[nums[j]] = 1
            else:
                dict_occurences[nums[j]] += 1
            i += 1
            j -= 1

        pairs = sorted([(dict_occurences[key], key) for key in dict_occurences])
        return [pairs.pop()[1] for i in range(k)]
