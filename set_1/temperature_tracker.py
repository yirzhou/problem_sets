import heapq, unittest


class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode
    def __init__(self):
        self.max = float('-inf')
        self.min = float('inf')
        self.mean, self.sum = 0, 0
        self.count_seen = {}
        self.temp_count = 0
        self.mode = None

    def insert(self, temperature):
        '''The original insert function takes O(Nlog(N)) time to 
        push each value into the heap.
        '''
        self.temp_count += 1
        self.sum += temperature

        if temperature not in self.count_seen:
            self.count_seen[temperature] = 0
        self.count_seen[temperature] += 1

        if not self.mode: self.mode = temperature
        else: self.mode = temperature if self.count_seen[temperature] > self.count_seen[self.mode] else self.mode

        self.mean = self.sum/self.temp_count
        self.max = max(self.max, temperature)
        self.min = min(self.min, temperature)

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)