from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1

        count = 0

        for c in freq.values():
            if c % 2 == 0:
                count += c
            else:
                count += c - 1

        if count < len(s):
            count += 1

        return count