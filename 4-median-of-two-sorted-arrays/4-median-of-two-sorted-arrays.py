class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if (l := len(nums1)) % 2:
            return nums1[l//2]
        else:
            return (nums1[l//2-1] + nums1[l//2])/2
