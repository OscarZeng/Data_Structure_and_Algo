#For only limited nums of elements, use count sort to do the problem
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0,0,0
        for i in nums:
            if i == 0:
                red += 1
            if i == 1:
                white += 1
            if i == 2:
                blue += 1
        reds = [0] * red
        white = [1] * white
        blues = [2] * blue
        nums[:] = reds + white + blues
        return
