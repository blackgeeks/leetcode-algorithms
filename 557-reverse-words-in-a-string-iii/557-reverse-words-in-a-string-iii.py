class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i, wrd in enumerate(words):
            words[i] = wrd[::-1]

        return " ".join(words)