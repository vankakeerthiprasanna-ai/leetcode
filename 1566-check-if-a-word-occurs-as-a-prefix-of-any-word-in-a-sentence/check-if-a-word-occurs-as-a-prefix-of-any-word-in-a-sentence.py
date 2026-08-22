class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        if sentence.startswith(searchWord):
            return 1
            
        count = 1
        for i in range(1, len(sentence)):
            if sentence[i - 1] == " ":
                if sentence[i:].startswith(searchWord):
                    return count 
                    
            if sentence[i] == " ":
                count = count + 1
                
        return -1
