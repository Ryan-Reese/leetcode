class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_count: int = 0
        char_loc: int = 0
        s2_idx: int = 0
        temp_s1: str = s1

        while s2_idx < len(s2):
            if s2[s2_idx] in temp_s1:
                char_count += 1
                char_loc = temp_s1.find(s2[s2_idx])
                if char_loc == (len(temp_s1) - 1):
                    temp_s1 = temp_s1[:char_loc]
                else:
                    temp_s1 = temp_s1[:char_loc] + temp_s1[char_loc + 1 :]
            else:
                char_count = 0
                s2_idx -= len(s1) - len(temp_s1)
                temp_s1 = s1
            if char_count == len(s1):
                return True
            s2_idx += 1
        return False
