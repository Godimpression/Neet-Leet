class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
    # Start by assuming the first word is the prefix
        prefix = strs[0]
    
        for i in range(1, len(strs)):
        # Keep shortening the prefix until it's found at the start of strs[i]
             while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                   return ""
                
        return prefix