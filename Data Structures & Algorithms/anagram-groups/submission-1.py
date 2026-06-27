class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for string in strs:
            sorted_string = str(sorted(string))
            if sorted_string not in hmap:
                hmap[sorted_string] = [string]
            else:
                hmap[sorted_string].append(string)
        
        return list(hmap.values())