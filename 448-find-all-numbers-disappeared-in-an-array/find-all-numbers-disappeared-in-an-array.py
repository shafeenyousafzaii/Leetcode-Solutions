class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        listt=[x for x in range(1,len(nums)+1)]
        listt.append(len(nums))
        listt=set(listt)
      
        return list(listt-set(nums))