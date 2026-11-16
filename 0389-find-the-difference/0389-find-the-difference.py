
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        count = {}

        # Count characters in s
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Check characters in t
        for ch in t:
            if ch not in count or count[ch] == 0:
                return ch

            count[ch] -= 1

