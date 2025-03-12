class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = [-1, -1, -1]
        count, right = 0, 0

        while right < len(s):
            abc[ord(s[right]) - ord('a')] = right
            minIndex = float('inf')

            for i in range(3):
                minIndex = min(minIndex, abc[i])

            count += (minIndex + 1)
            right += 1
            
        return count