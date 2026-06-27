class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            sorted_s = sorted(s)
            if str(sorted_s) not in hmap:
                hmap[str(sorted_s)] = [s]
        
            else:
                hmap[str(sorted_s)].append(s)
        return list(hmap.values())