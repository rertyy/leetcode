// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2) + int(b,2)
        return str(bin(x)).replace("0b","")