class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max = None
        
        for sentence in sentences:
            words = sentence.split()
            count = len(words)
            
            if max == None:
                max = count
            if count > max:
                max = count
                
        return max