from collections import defaultdict


def def_value():
    return 0


class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:
        if len(str1) != len(str2):
            return False

        count_dict_str1, count_dict_str2 = defaultdict(def_value), defaultdict(
            def_value
        )

        for i in range(len(str1)):
            count_dict_str1[str1[i]] += 1
            count_dict_str2[str2[i]] += 1
        for count in count_dict_str1:
            if count_dict_str1[count] != count_dict_str2[count]:
                return False
        return True
