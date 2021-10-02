# 1103. Distribute Candies to People

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        iteration = 0
        people = [0 for _ in range(num_people)]
        while candies > 0:
            i = 0
            while i < len(people):
                num = i + 1 + len(people) * iteration
                if num <= candies:
                    people[i] += num
                    candies -= num
                else:
                    people[i] += candies
                    candies = 0
                i += 1
            iteration += 1
        return people