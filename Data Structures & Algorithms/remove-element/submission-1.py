class Solution:
   # Two ptr
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] != val):
            return 0
        
        if len(nums) == 1 and nums[0] == val:
            nums.pop()
            return 1

        curr_idx = 0
        next_idx = 0

        while next_idx < len(nums) and curr_idx < len(nums):
            print(nums)
            print("curr_idx", curr_idx)
            print("next_idx", next_idx)
            if nums[curr_idx] == val:
                while nums[next_idx] == val or next_idx <= curr_idx:
                    next_idx += 1
                    print("new next_idx1", next_idx)

                    if next_idx == len(nums):
                        nums = nums[:curr_idx]
                        return curr_idx
                
                print("new next_idx2", next_idx)

                nums[curr_idx] = nums[next_idx]
                nums[next_idx] = val

                curr_idx += 1
            else:
                curr_idx += 1

        nums = nums[:curr_idx]
        print("nums", nums)
        print("k", curr_idx)
        return curr_idx