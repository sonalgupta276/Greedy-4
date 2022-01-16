class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sl = len(source)
        tl = len(target)
        hashmap = {}
        for j in range(sl):
            if source[j] not in hashmap:
                hashmap[source[j]] = list()
            hashmap[source[j]].append(j)
        i, pos = 0, 0
        result = 0
        while i < tl:
            
            if target[i] not in hashmap:
                return -1
            while pos < sl and source[pos] != target[i]:
                pos += 1
            if pos == sl:
                result += 1
                pos = 0
            else:
                i += 1
                pos += 1
        return result + 1
        
# Time Complexity: O(sl + tl)
# Space Complexity: O(1)

import bisect
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sl = len(source)
        tl = len(target)
        hashmap = {}
        for j in range(sl):
            if source[j] not in hashmap:
                hashmap[source[j]] = list()
            hashmap[source[j]].append(j)
        i, pos = 0, 0
        result = 0
        while i < tl:
            if target[i] not in hashmap:
                return -1
            ll = hashmap.get(target[i])
            k = bisect.bisect_left(ll, pos)
            # when pos is not present in ll , k == len(ll)
            if k == len(ll):
                result += 1
                pos = 0
            else:
                pos = ll[k] + 1
                i += 1       
        return result + 1

# Time Complexity: O(log(sl) + tl)
# Space Complexity: O(1)
    