class Solution(object):
    def __init__(self): self.max_val = 0

    def max_duffel_bag_value(self, cake_tuples, weight_capacity):
        return self.__max_bottom_up(cake_tuples, weight_capacity)

    def __max(self, begin, tuples, target, stack, current_sum, current_value):
        """This is the brute-force recursive solution.
        """
        if target == 0: 
            self.max_val = max(self.max_val, current_sum)
            return
        if target < 0: 
            self.max_val = max(self.max_val, current_sum-current_value)
            return

        for i in range(begin, len(tuples)):
            weight, monetary_value = tuples[i]
            if weight == 0: 
                if monetary_value > 0:
                    self.max_val = float('inf')
                    return 
                else: 
                    stack = []
                    continue
            stack.append(weight)
            current_sum += monetary_value
            self.__max(i, tuples, target-weight, stack, current_sum, monetary_value)
            stack.pop()
            current_sum -= monetary_value
        return 

    def __max_bottom_up(self, tuples, capacity):
        """This is a bottom-up approach.
        1. Main idea is that we start from the smallest capacity, say, 1kg.
        2. We gradually increase the capacity to the target capacity.
        3. For each capacity, we only care about the weights below the capacity.
        """
        monetary_vals = [0]*(capacity+1)
        monetary_combos = []
        for _ in range(capacity+1): monetary_combos.append([])
        for current_capacity in range(1, capacity+1):
            for weight, value in tuples:
                if weight == 0:
                    if value == 0: continue
                    else: return float('inf')
                if weight <= current_capacity:
                    if monetary_vals[current_capacity-weight]+value > monetary_vals[current_capacity]:
                        monetary_combos[current_capacity] = []
                        for val in monetary_combos[current_capacity-weight]:
                            monetary_combos[current_capacity].append(val)
                        monetary_combos[current_capacity].append(weight)
                    monetary_vals[current_capacity] = max(monetary_vals[current_capacity-weight]+value, monetary_vals[current_capacity])
        return monetary_vals[capacity], monetary_combos[capacity]

def main():

    total_weight, combos = Solution().max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
    print(total_weight)
    print(combos)

if __name__ == '__main__': main()