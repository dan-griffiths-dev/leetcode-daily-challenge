

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # sort the list

        nums.sort()
        ans = []
        seen = set()
        n = len(nums)

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    triplet = (nums[i], nums[left], nums[right])
                    if triplet not in seen:
                        seen.add(triplet)
                        ans.append(list(triplet))

                    left += 1
                    right -= 1
                    

                elif total < 0:
                    left += 1

                else:
                    right -= 1
        
        return ans

       