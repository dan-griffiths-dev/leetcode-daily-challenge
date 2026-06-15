# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/



class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:


        n = len(nums)
        nums.sort()

        MOD = 10 ** 9 + 7

        # prepare powers of 2 to avoid recalculating in the loop
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = pow2[i-1] * 2 % MOD

        ans = 0
        left = 0
        right = n -1

        while left <= right:
            if nums[left] + nums[right] <= target:

                # nums[left] is fixed as min, nums[right] is fixed as max
                # everythall elements in between (left+1 ... right) have two opions from pov of sequence 1. included or 2. not included
                # = 2^(right - left) subsequences

                ans = (ans + pow2[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return ans
    

    """ 
        Notes:
            1. a fixed window misses non-contiguous subsequences
            sorted: [1, 2, 3, 4]

            window [1, 2, 3] captures: {1,2}, {1,3}, {1,2,3} etc.
            but misses:        {1, 4}, {1, 2, 4}, {1, 3, 4} ...
                                    ^ skips over 2 or 3
     
            2.  modulo 10⁹ + 7"
            The answer is a count of subsequences. 
            With n elements, the max possible count is 2^n — every element in or out. 
            For n = 100,000 (leetcode constraint), that's:  2^100000 = a number with ~30,000 digits

            3. Using mod
            instead of tracking a 30,000 digit number, you always have a number between 0 and 10⁹+6. Fits in a standard 32-bit integer.
            Why 10⁹ + 7 specifically?

                prime number — offers math properties that make it safe to use in modular arithmetic (division, inverse operations work cleanly)
                It's just under 2^30 — fits comfortably in 32 bits, and two of them multiplied fit in 64 bits without overflow
                
    """


        
        