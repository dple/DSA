"""
Leetcode 49: https://leetcode.com/problems/group-anagrams/description/
"""
class Solution:
    def ground_anagrams(self, strs):
        ans = {}

        for s in strs:
            s_sorted = ''.join(sorted(s))            

            if s_sorted not in ans:
                ans[s_sorted] = [s]
            else:
                ans[s_sorted].append(s)

        return [value for value in ans.values()]

sol = Solution()
strs = ["tea", "eat", "tan", "ate", "nat", "bat"]

print(sol.ground_anagrams(strs))