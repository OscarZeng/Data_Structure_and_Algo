class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1Copy = nums1[:m].copy()
        #Simply remember this very unique way of renewing nums1
        nums1[:] = []
        idx1, idx2 =0,0
        while idx1 < m and idx2 < n:
            if nums1Copy[idx1] <= nums2[idx2]:
                nums1.append(nums1Copy[idx1])
                idx1 += 1
            else:
                nums1.append(nums2[idx2])
                idx2 += 1
            #print(nums1)
        if idx1 == m and idx2 == n:
            return
        if idx1 == m:
            nums1 += nums2[idx2:]
        if idx2 == n:
            nums1 += nums1Copy[idx1:]
        #print(nums1)