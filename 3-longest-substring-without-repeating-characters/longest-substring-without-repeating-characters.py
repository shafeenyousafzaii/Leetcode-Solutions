class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        window = s[0]
        curr = s[0]

        for i in range(1,len(s)):
            for j in range(i,len(s)):
                if s[j] not in curr:
                    curr += s[j]
                else:
                    break

            if len(curr) > len(window):
                window = curr
            curr = s[i]

        return len(window)