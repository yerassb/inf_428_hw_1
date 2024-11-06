class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        c1 = 0
        c2 = 0
        ans = []
        for i in range(0, m + n + 1):
            if c1 == m:
                if c2 == n: break
                ans.append(nums2[c2])
                c2 += 1
                continue
            elif c2 == n:
                if c1 == m: break
                ans.append(nums1[c1])    
                c1 += 1
                continue
            if nums1[c1] >= nums2[c2]:
                ans.append(nums2[c2])
                c2 += 1
            else:
                ans.append(nums1[c1])
                c1 += 1
        for i in range(len(nums1)):
            nums1[i] = ans[i]       
    
        
            
        