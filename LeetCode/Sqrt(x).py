class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, ans = 0, x, 1
        while(left <= right):
            mid = (right + left) // 2;
            if mid * mid == x:
                return mid
            elif mid*mid < x:
                ans = mid
                left = mid +1
                
            else:
                right = mid -1
        return ans
