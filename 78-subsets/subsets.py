class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_list=[[]]
        for i in nums:
            new_subset=[]
            for items in curr_list:
                new_subset.append(items+[i])
            curr_list.extend(new_subset)
        return curr_list
