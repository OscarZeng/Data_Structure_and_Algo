class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n , A, B= len(nums1), len(nums2), nums1, nums2
        #Assume that n is the bigger one
        if n < m:
           n,m ,B, A = len(nums1), len(nums2), nums1, nums2
        half_len = (m+n+1)//2
        imax = m
        imin = 0
        while imin <= imax:
            i = (imax+imin)//2
            #This fixed the total length of i + j, which is the left part
            j = half_len - i
            #While we konw that the left part will always be smaller than the right part
            #Which is B[j-1] < A[i] and A[i-1] < B[j](Since we already konw that A[i-1]<= A[i]and B[j-1]< B[j])
            # Here when i reachs the end of the begin of the array we can stop searching since the middle number must in the other array
            if i < m and B[j-1] > A[i]:
            #i is too small, i must be atleast from i
                imin = i + 1
            elif i > 0 and B[j] < A[i-1]:
            #j is too small, which means i is too bigger
                imax = i -1
            #in this case the i is at the right place
            else:    

                if i == 0: 
                    leftmax = B[j-1]
                elif j == 0:
                    leftmax = A[i-1]
                else:
                    leftmax = max(B[j-1], A[i-1])
                
                if (m + n)%2 ==1:
                    return leftmax

                if i == m:
                    rightmin = B[j]
                elif j == n:
                    rightmin = A[i] 
                else:
                    rightmin = min(B[j], A[i])
                return (rightmin + leftmax)/2.0

#Sample Solution:
def median(A, B):
    m, n = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m
    if n == 0:
        raise ValueError

    imin, imax, half_len = 0, m, (m + n + 1) / 2
    while imin <= imax:
        i = (imin + imax) / 2
        j = half_len - i
        if i < m and B[j-1] > A[i]:
            # i is too small, must increase it
            imin = i + 1
        elif i > 0 and A[i-1] > B[j]:
            # i is too big, must decrease it
            imax = i - 1
        else:
            # i is perfect

            if i == 0: max_of_left = B[j-1]
            elif j == 0: max_of_left = A[i-1]
            else: max_of_left = max(A[i-1], B[j-1])

            if (m + n) % 2 == 1:
                return max_of_left

            if i == m: min_of_right = B[j]
            elif j == n: min_of_right = A[i]
            else: min_of_right = min(A[i], B[j])

            return (max_of_left + min_of_right) / 2.0
           