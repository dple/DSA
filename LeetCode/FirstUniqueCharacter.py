"""
Given a string, return the index of the first unique characteer in the string
For ex:
Given: Leetcode
Return: 0 (as L is the first unique character)
Given LoveLeetcode
Return: 2 (as v is the first unique character)
"""

class Solution:
    def first_unique_char(self, s: str) -> int:
        characters = {}         # Hash map storing character and its last position in the string
        for i, c in enumerate(s):
            characters[c] = i
        
        '''
        # Rescan the hash map to get the lowest position 
        res = (None, len(s))
        for key, value in characters.items():
            if value < res[1]:
                res = (key, value)
        '''
        # Sort the hash map by value 
        sorted_chac = sorted(characters.items(), key = lambda kv: (kv[1], kv[0]))
        return sorted_chac[0]
    

s = "LoveLeetcode"
sol = Solution()
print("First unique character and its position:", sol.first_unique_char(s))
