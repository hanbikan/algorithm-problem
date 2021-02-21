class Solution:
    def containsDuplicate(self, nums):
        dict_num = {}
        for num in nums:
            if dict_num.get(num):
                return True
            else:
                dict_num[num] = True
        return False
nums = [1,1,1,3,3,4,3,2,4,2]
s = Solution()
print(s.containsDuplicate(nums))