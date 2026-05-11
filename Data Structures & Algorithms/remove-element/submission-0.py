class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        elemsRemoved = 0
        for i in range(len(nums)):
            realIndex = i - elemsRemoved
            
            if nums[realIndex] == val:
                nums.pop(realIndex)
                elemsRemoved += 1
        
        return len(nums)