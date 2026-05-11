class Solution:
    def jumpToNextNonValIdx(self, nums: List[int], val: int, idx: int) -> int:
        while idx < len(nums):
            if nums[idx] == val:
                idx += 1
            else:
                return idx
        
        return -1

    # Simpler 2-ptr
    def removeElement(self, nums: List[int], val: int) -> int:
        k_idx = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == val:
                k_idx = self.jumpToNextNonValIdx(nums, val, i)

                if k_idx == -1:
                    return count

                nums[i] = nums[k_idx]
                nums[k_idx] = val
                print(nums)
            
            count += 1

        return count
