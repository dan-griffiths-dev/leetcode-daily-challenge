

def judgeSquareSum(self, c: int) -> bool:


        # create array numbers between 0 and c-1
        nums = []
        for i in range(1, c):
            nums.append(i)
        
        a = 0
        b = int(c**0.5)
        while a <= b:
            total = a**2 + b**2

            if total == c:
                return True
            elif total < c:
                a += 1
            elif total > c:
                b -= 1
        
        return False


""" 
    two pointers:
        a starts at 0
        b starts at sqrt(c)  =>  b**0.5

        if a² + b² = c, then neither a nor b can exceed √c.
        recognise this as a bounded search space [0, √c] which the pointers can move between similarly to Two Sum II:
            if a² + b² == c  → True
            if a² + b² < c   → a++
            if a² + b² > c   → b--

"""