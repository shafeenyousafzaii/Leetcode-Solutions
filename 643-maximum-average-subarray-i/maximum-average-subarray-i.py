class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        window_sum=(sum(nums[:k]))
        max_avg=window_sum
        for i in range(k,len(nums)):
            window_sum=(window_sum+nums[i] - nums[i-k])
            # max_avg=max(window_sum,max_avg)
            if max_avg < window_sum:
                max_avg=window_sum
        return max_avg / float(k)


        