class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        for i in s:
            if s==t:
                return True
            else:
                return False
---------------------------------------------------------


from collections import defaultdict


def anagrams(string1, string2):
    dict1 = to_dict(string1)
    dict2 = to_dict(string2)
    return dict1 == dict2

def to_dict(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d
