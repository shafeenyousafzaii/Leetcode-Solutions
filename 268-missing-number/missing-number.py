class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        for k in range(len(nums)):
            # if k!= minn:
            #     return k
            if k!=nums[k]:
                return k
            # continue
        return (len(nums))