class Solution:
    def  __init__(self):
        pass
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))
        print("nums:",nums,"   factorials:",factorials)
        # fit k in the interval 0 ... (n! - 1)
        k -= 1
        
        # compute factorial representation of k
        output = [] 
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]
            print("idx:", idx, "  k:", k, "i",i)
            
            output.append(nums[idx])
            print("output:", output)
            del nums[idx]
            print("nums:", nums)
        
        return ''.join(output)

if __name__ == '__main__':
    s = Solution()
    n = 7
    k = 10
    s.getPermutation(n,k)