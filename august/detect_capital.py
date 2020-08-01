class Solution:
    """#520. Given a word, you need to judge whether the usage of capitals in it is right or not.

    We define the usage of capitals in a word to be right when one of the following cases holds:

    1. All letters in this word are capitals, like "USA".
    2. All letters in this word are not capitals, like "leetcode".
    3. Only the first letter in this word is capital, like "Google".
    
    Otherwise, we define that this word doesn't use capitals in a right way.
    """
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].islower():
            for char in word:
                if char.isupper(): return False
        else:
            count = 0
            for char in word:
                if char.isupper(): count += 1
            return count == 1 or count == len(word)
        return True
            