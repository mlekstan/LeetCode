class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        if m == 0:
            nums1[m:n] = nums2[m:n]
            return
        if n == 0:
            return
        
        if nums1[m-1] < nums2[n-1]:
            nums1[m-1+n] = nums2[n-1]
            self.merge(nums1, m, nums2, n-1)

        else:
            nums1[m-1+n] = nums1[m-1]
            self.merge(nums1, m-1, nums2, n)
        

A = [0]
B = [1]

Solution().merge(A, len(A)-len(B), B, len(B))
print(A)
        