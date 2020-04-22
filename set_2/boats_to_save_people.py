import heapq

class Solution:
    '''The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

    Each boat carries as many people at the same time as possible, provided the sum of the weight of those people is at most limit.

    Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)
    '''
    def num_rescue_boats(self, people, limit):
        '''The intuition is that we pair the lightest people with the heaviest person.
        Since the lightest people can pair with anyone, they might just sit with
        the heaviest peerson. 
        Time: O(Nlog(N))
        Space: O(1) if the sorting is in-place, 
        '''
        weights = sorted(people)
        light, heavy = 0, len(weights)-1
        
        count = 0
        while light <= heavy:
            remained = limit - weights[heavy]
            count += 1
            while light < heavy and weights[light] <= remained:
                remained -= weights[light]
                light += 1
            heavy -= 1
        return count

    def num_rescue_boats_faster(self, people, limit):
        '''Same intuition, but trades space for time.
        Space: O(L), L is the limit.
        Time: O(L), L is the limit.
        '''
        weights = [0]*(limit+1)

        for weight in people: weights[weight] += 1
        count, light, heavy = 0, 1, limit

        while light <= heavy:
            while heavy >= light and weights[heavy] <= 0: heavy -= 1
            if heavy < light: break
            weights[heavy] -= 1
            count += 1
            while heavy >= light and weights[light] <= 0: light += 1

            remained = limit - heavy
            if light <= remained: weights[light] -= 1
            

        return count

print(Solution().num_rescue_boats_faster([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10], 50))
print(Solution().num_rescue_boats_faster([3,5,3,4], 5))
print(Solution().num_rescue_boats_faster([1,2,4,5], 6))
