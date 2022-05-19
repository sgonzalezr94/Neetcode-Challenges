from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult_list = list()
        mult_dict = dict()
        i = 0
        while i < len(nums):
            if nums[i] not in mult_dict:
                tmp_list = nums[0:i] + nums[i + 1 :]
                if 0 in tmp_list:
                    mult_list.append(0)
                    mult_dict[nums[i]] = 0
                else:
                    a = 1
                    for c in tmp_list:
                        a *= c
                    mult_list.append(a)
                    mult_dict[nums[i]] = a
            else:
                mult_list.append(mult_dict[nums[i]])

            i += 1
        return mult_list
