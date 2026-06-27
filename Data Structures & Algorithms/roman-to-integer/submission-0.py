class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            "I" : 1,
            "V" : 5,
            "X": 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        s = list(s)
        ans = 0
        i = 0

        while i < len(s):
            to_add = 0
            if (i+1 < len(s) ) and (( s[i] == "I" and s[i+1] == "V" ) or ( s[i] == "I" and s[i+1] == "X")):
                to_add = hmap[s[i+1]] - 1 
                i += 2
            elif (i+1 < len(s) ) and (( s[i] == "X" and s[i+1] == "L" ) or ( s[i] == "X" and s[i+1] == "C")):
                to_add = hmap[s[i+1]] - 10
                i+=2
            elif (i+1 < len(s) ) and (( ( s[i] == "C" and s[i+1] == "D" ) or ( s[i] == "C" and s[i+1] == "M"))):
                to_add = hmap[s[i+1]] - 100
                i+=2
            else:
                to_add = hmap[s[i]]
                i+=1

            ans += to_add

        return ans