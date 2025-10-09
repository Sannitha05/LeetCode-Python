from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
       
        common_count = [0] * 26
        for c in words[0]:
            common_count[ord(c) - ord('a')] += 1

        
        for word in words[1:]:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            for i in range(26):
                common_count[i] = min(common_count[i], count[i])

     
        result = []
        for i in range(26):
            result.extend([chr(i + ord('a'))] * common_count[i])

        return result
