import unittest

class Solution(object):
    def __init__(self): return

    def string_shift(self, string, shift):
        if len(shift) == 0 or len(string) < 2: return string
        net_right_shifts = self.get_net_shift(shift)
        shifted_string = list(string)
        length = len(shifted_string)

        if net_right_shifts == 0: return string
        net_right_shifts %= length

        if net_right_shifts > 0:
            buffer = shifted_string[length-net_right_shifts:]
            for i in range(length-net_right_shifts-1, -1, -1):
                shifted_string[i+net_right_shifts] = shifted_string[i]
            for j in range(len(buffer)): 
                shifted_string[j] = buffer[j]
        else:
            net_left_shifts = -1*net_right_shifts
            buffer = shifted_string[:net_left_shifts]
            for i in range(net_left_shifts, length):
                shifted_string[i-net_left_shifts] = shifted_string[i]
            for j in range(len(buffer)):
                shifted_string[length-net_left_shifts+j] = buffer[j]
        return ''.join(shifted_string)

    def get_net_shift(self, shift):
        net_right_shifts = 0
        for item in shift:
            direction, amount = item[0], item[1]
            if direction == 0: net_right_shifts -= amount
            else: net_right_shifts += amount
        return net_right_shifts

class Test(unittest.TestCase):
    def test_right_short(self):
        self.assertEqual('cdefgab', Solution().string_shift('abcdefg', [[0,2]]))

unittest.main(verbosity=2)
