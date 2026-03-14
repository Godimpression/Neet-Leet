class Solution:
    def rob(self, nums: List[int]) -> int:
        adj_1=0
        adj_2=0
        for num in nums:
            adj_1, adj_2 = adj_2, max(adj_2, adj_1 + num)
        return adj_2

            

        