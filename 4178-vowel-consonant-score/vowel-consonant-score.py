class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels=["a","e","i","o","u"]
        count_vow=[]
        count_consonant=[]
        for i in s:
            if i.isalpha():               
                if i in vowels:
                    count_vow.append(i)
                else:
                    count_consonant.append(i)
        v=len(count_vow)
        c=len(count_consonant)
        if c == 0 or v==0:
            return 0 
        return v // c

