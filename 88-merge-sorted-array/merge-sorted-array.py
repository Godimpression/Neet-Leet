class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x = m-1
        y= n-1
        b= m+n -1

        while x>= 0 and y>=0:
            if nums1[x] > nums2[y]:
                nums1[b] = nums1[x]
                x-=1
            else:
                nums1[b] = nums2[y]
                y-=1
            b-=1

        nums1[:y + 1] = nums2[:y + 1]
