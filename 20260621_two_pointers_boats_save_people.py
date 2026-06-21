def numRescueBoats(self, people: List[int], limit: int) -> int:

        # max 2 people / boat
        # even number peope or odd number of people
        # sort list


        people.sort()
        n = len(people)
        left = 0
        right = n - 1
        boats = 0
        while left < right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            elif people[left] + people[right] > limit:
                boats += 1
                right -= 1
        
        # odd number of people leaves 1 person
        if left == right:
            boats += 1
        
        return boats