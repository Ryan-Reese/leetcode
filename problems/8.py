from ctypes import c_int32


class Solution:
    def myAtoi(self, s: str) -> int:
        # whitespace
        s = s.lstrip()
        if s == "":
            return 0
        # signedness
        if s[0] in ["-", "+"]:
            sign = 1 if (s[0] == "+") else -1
            s = s[1:]
        else:
            sign = 1
        # conversion
        for i in range(1, len(s) + 1):
            if not (s[:i].isdigit()):
                s = s[: (i - 1)]
                break
        # rounding
        if s == "":
            return 0
        s = int(s) * sign
        if s > ((2**31) - 1):
            return (2**31) - 1
        if s < (-(2**31)):
            return -(2**31)
        return s
