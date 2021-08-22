# 482. License Key Formatting

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        i = len(s) - k
        while i > 0:
            s = s[:i] + '-' + s[i:]
            i -= k
        return s