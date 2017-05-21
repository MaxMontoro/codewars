import unittest

from katas.pick_peaks import *

class TestPickPeaks(unittest.TestCase):
    def test_simple_peak(self):
        self.assertEqual(pick_peaks([1,2,2,2,3,4,5,9,8,6,2,1]), {"pos": [7], "peaks": [9]})

    def test_two_peaks(self):
        self.assertEqual(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})

    def test_ignore_peaks_at_edges(self):
        self.assertEqual(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})

    def test_start_of_plateau_is_returned(self):
        self.assertEqual(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
