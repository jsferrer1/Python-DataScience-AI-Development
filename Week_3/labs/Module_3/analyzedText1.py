class analysedText(object):
    
    def __init__ (self, text):

        # Remove the punctuation from <text> and make it lower case.
        text = text.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text = text.replace(ch, " ")

        # Assign the formatted text to a new attribute called "fmtText"
        self.fmtText = text
        
        pass 
    
    def freqAll(self):    

        # Split the text into a list of words  
        wordList = self.fmtText.split()

        # Create a dictionary with the unique words in the text as keys
        # and the number of times they occur in the text as values
        wordDict = {}
        for word in wordList:
            if word not in wordDict:
                wordDict[word] = 1
            else:
                wordDict[word] += 1
      
        self.freqText = wordDict

        pass # return the created dictionary
    
    def freqOf(self, word):

        # return the number of occurrences of <word> in <fmtText>
        return self.freqText[word]
