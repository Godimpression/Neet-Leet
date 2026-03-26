class Autocorrect:
    def __init__(self, words):
        # Store as a set for O(1) exact match lookups
        self.dictionary = set(words)

    def correct(self, word):
        # 1. Exact match check
        if word in self.dictionary:                           
            return word
        
        # 2. Look for a "one character different" match
        for dict_word in self.dictionary:
            if len(dict_word) == len(word):                       
                mismatches = 0
                for i in range(len(word)):
                    if word[i] != dict_word[i]:
                        mismatches += 1
                    
                    # Optimization: stop if we already found 2+ differences
                    if mismatches > 1:
                        break
                
                if mismatches == 1:
                    return dict_word
        
        # 3. No match found, return the original word per requirements
        return word

# Test it
corrector = Autocorrect(["apple", "pear", "orange"])
print(corrector.correct("apply"))  # Output: apple (1 mismatch)
print(corrector.correct("apples")) # Output: apples (Different length)
print(corrector.correct("bear"))   # Output: pear (1 mismatch)
