class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev = {}
        for index in range(0, len(nums)):
            find = target-nums[index]
            if find in prev:
                return [prev[find], index]
            prev[nums[index]] = index

if __name__ == '__main__':
    obj = Solution()
    result_lst = obj.twoSum([2,7,11,15], 9)
    result_lst = obj.twoSum([3,2,4], 6)
    print(result_lst)