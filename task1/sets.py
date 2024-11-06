class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ansset = set()
        set1 = set(nums1)
        for num in nums2:
            if num in set1:
                ansset.add(num)
        
        return list(ansset)

        