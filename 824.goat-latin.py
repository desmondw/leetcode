#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        output = []
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        for i,word in enumerate(sentence.split(' ')):
            if word[0] not in vowels:
                word = word[1::] + word[0]
            word = word + 'ma'

            word = word + 'a'*(i+1)
            output.append(word)
        return ' '.join(output)

# @lc code=end

