# The pattern scales cleanly:

# 3Sum → 1 outer loop + two pointers → O(n²)
# 4Sum → 2 outer loops + two pointers → O(n³)
# kSum → (k-2) outer loops + two pointers → O(nᵏ⁻¹)




class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        ans = []
        n = len(nums)
        seen = set()

        for i in range(n-3):
            for j in range(i+1, n-2):

                left = j+1
                right = n-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        quad = (nums[i], nums[j], nums[left], nums[right])
                        if quad not in seen:
                            seen.add(quad)
                            ans.append(list(quad))
                        left += 1
                        right -=1

                    elif total < target:
                        left +=1
                    else:
                        right-=1
        
        return ans