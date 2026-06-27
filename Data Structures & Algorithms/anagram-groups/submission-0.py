class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        if not strs:
            return []

        for i in strs:
            if tuple(sorted(i)) in hmap.keys():
                hmap[tuple(sorted(i))].append(i)
            else:
                hmap[tuple(sorted(i))] = [i]
        
        return list(hmap.values())