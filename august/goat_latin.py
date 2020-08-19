class Solution:
    """#824. A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

    We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

    The rules of Goat Latin are as follows:

    - If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word. For example, the word 'apple' becomes 'applema'.
    
    - If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma". For example, the word "goat" becomes "oatgma".
    
    - Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1. For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
    Return the final sentence representing the conversion from S to Goat Latin. 
    """
    def toGoatLatin(self, S: str) -> str:
        tmp = []
        ans = " "
        i = 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        words = S.split(" ")
        for word in words:
            if word[0] in vowels: word += "ma"
            else: word = word[1:]+word[0]+"ma"
            word += "a"*i
            i += 1
            tmp.append(word)
        return ans.join(tmp)
