class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        acc = 0

        for i, num in enumerate(nums):
            lastNum = nums[i - 1] if i != 0 else 0

            # Current num is 1
            if num == 1 and lastNum == 1:
                acc += 1
            
            if num == 1 and lastNum == 0:
                acc = 1
            
            # Current num is not 1 or reached end
            if i == len(nums) - 1 or num == 0:
                if acc > maxOnes:
                    maxOnes = acc
                
                acc = 0
        
        return maxOnes