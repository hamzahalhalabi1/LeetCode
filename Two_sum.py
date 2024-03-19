class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: in,t
        :rtype: List[int]
        """

        map = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in map:
                return [map[complement], index]
            map[number] = index
        return []


solution = Solution()
x = solution.twoSum([2, 4, 6, 9], 15)
print(x)
