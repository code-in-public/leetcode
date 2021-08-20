#!/usr/bin/env python3

class Solution:
    """
        nums = [0,1,0,3,12]

        nums = [0,1,0,3,12]
                Z V



    while idx <= len {
      idx++
      if delta = 0
        continue
      if val[idx] != 0
        val[idx - delta] = val[idx]
        continue;
      delta +1
   } while delta >= 0 { val[idx - delta] = 0
    delta--}


    """
    def moveZeros(self, nums):
        left_zero_idx = None # idx of left most zero
        value_idx = None # idx of a value needing to shift

        current_idx = 0

        print(nums)

        while current_idx < len(nums):
            if left_zero_idx is None and nums[current_idx] == 0:
                # Found the left most 0
                left_zero_idx = current_idx
            elif left_zero_idx >= 0 and nums[current_idx] != 0:
                # Perform swap and clear left_zero_idx
                value_idx = current_idx

                nums[left_zero_idx] = nums[value_idx]
                nums[value_idx] = 0

                left_zero_idx = left_zero_idx + 1

            current_idx += 1

        return nums
