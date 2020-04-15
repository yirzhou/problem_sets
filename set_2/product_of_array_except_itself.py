class Solution(object):
    def __init__(self): return

    def product_of_array_except_itself(self, nums):

        if len(nums) < 2: return nums

        if len(nums) == 2: return [nums[1], nums[0]]

        results = [1]*len(nums)
        temp = 1

        for index in range(1, len(nums)):
            temp *= nums[index-1]
            results[index] = temp

        temp = 1
        for index in range(len(nums)-2, -1, -1):
            temp *= nums[index+1]
            results[index] *= temp

        return results

def main():
    print(Solution().product_of_array_except_itself([1,2,3,4]))

if __name__ == '__main__': main()
        