class Solution:
    def sortSentence(self, s: str) -> str:
        words: dict[int, str] = {int(word[-1]): word[:-1] for word in s.split()}
        output: str = ""
        for i in range(len(words)):
            if i != (len(words) - 1):
                output += f"{words[i + 1]} "
            else:
                output += words[i + 1]
        return output
