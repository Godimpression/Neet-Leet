class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ''' args
        s is a sring and spaces will be added to it
        spaces tell the indices where a space will be added'''
        splits=[]
        last_ind=0
        for i in range (0,len(spaces)):
            a=s[last_ind:spaces[i]]
            b=' '
            new= a+b
            splits.append(new)
            last_ind=spaces[i]
        end_part=s[spaces[i]:]
        splits.append(end_part)
        return "".join(splits)

        
        