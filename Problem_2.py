from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if tops == None or len(tops) == 0:
            return 0
        hashmap = {}
        maximum = -1
        for i in range(len(tops)):
            hashmap[tops[i]] = hashmap.get(tops[i], 0) + 1
            if hashmap[tops[i]] >= len(tops):
                maximum = tops[i]
            hashmap[bottoms[i]] = hashmap.get(bottoms[i], 0) + 1
            if hashmap[bottoms[i]] >= len(tops):
                maximum = bottoms[i]
        if maximum == -1:
            return -1
        aRot = 0
        bRot = 0
        for i in range(len(tops)):
            if tops[i] != maximum and bottoms[i] != maximum:
                return -1
            if tops[i] != maximum:
                aRot += 1
            if bottoms[i] != maximum:
                bRot += 1
        return min(aRot, bRot)

# without hashmap
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if tops == None or len(tops) == 0:
            return 0
        result = self.check(tops, bottoms, tops[0])
        if result != -1:
            return result
        return self.check(tops, bottoms, bottoms[0])
    
    def check(self, tops: List[int], bottoms: List[int], target) -> int:
        aRot = 0
        bRot = 0
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return -1
            if tops[i] != target:
                aRot += 1
            if bottoms[i] != target:
                bRot += 1
        return min(aRot, bRot)

# Time Complexity: O(n)
# Space Complexity: O(1)