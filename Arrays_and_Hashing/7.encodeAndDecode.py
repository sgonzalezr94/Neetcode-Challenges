import re
from typing import List


class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs: List[str]) -> str:
        str_out = str()
        for string in strs:
            str_out += string + ";"
        return str_out

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """

    def decode(self, str: str) -> List[str]:
        return [i for i in str.split(";") if i]
