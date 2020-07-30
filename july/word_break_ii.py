class Solution:
    """#140. Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
    add spaces in s to construct a sentence where each word is a valid dictionary word. 
    Return all such possible sentences.

    Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.
    """
    def wordBreak(self, s: str, wordDict):
        words = set(wordDict)
        memo = {}
        def word_break(s):
            if s in memo: return memo[s]
            res = []
            
            if s in words: res.append(s)
            for i in range(1, len(s)):
                right = s[i:]
                if right not in words: continue
                res += [w + " " + right for w in word_break(s[0:i])]
            memo[s] = res
            return memo[s]
        return word_break(s)
        