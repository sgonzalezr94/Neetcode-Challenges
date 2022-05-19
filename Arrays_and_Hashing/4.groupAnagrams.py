from typing import List


class Solution:
    def create_count_dict(self, str: str) -> dict:
        str_dict = dict()
        for character in str:
            if character not in str_dict:
                str_dict[character] = 1
            else:
                str_dict[character] += 1
        return str_dict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_dict = dict()
        for str_in in strs:
            sorted_str = str(sorted(str_in))
            if sorted_str not in count_dict:
                count_dict[sorted_str] = [self.create_count_dict(sorted_str), [str_in]]
            else:
                count_dict[sorted_str][1].append(str_in)
        return [strs[1] for strs in count_dict.values()]
