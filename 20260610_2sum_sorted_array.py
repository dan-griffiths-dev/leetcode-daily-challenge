# 

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/2028889094/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # use two pointers beginning at either end of array
        # respect constant space requirement by returning [] immediately


        n = len(numbers)    # 4
        left = 0 
        right = n - 1     # 3

        while right > left:

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            
            elif numbers[left] + numbers[right] > target:
                right -= 1
            
            else:
                left += 1