# brute force approach


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perms: list[str] = self.generatePermutations(s1)
        for perm in perms:
            if perm in s2:
                return True
        return False

    def generatePermutations(self, s: str) -> list[str]:
        if len(s) == 1:
            return [s]
        else:
            output: list[str] = []
            idx: int = 0
            while idx < (len(s) - 1):
                output.extend(
                    [
                        s[idx] + perm
                        for perm in self.generatePermutations(s[:idx] + s[idx + 1 :])
                    ]
                )
                idx += 1
            output.extend(
                [s[idx] + perm for perm in self.generatePermutations(s[:idx])]
            )
            return output
