class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new = sorted(nums1 + nums2)
        n = len(new)
        
        if n % 2 != 0:
            return float(new[n // 2])
        else:
            return (new[(n // 2) - 1] + new[n // 2]) / 2