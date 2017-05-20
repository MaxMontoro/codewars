from tests.test_helpers import *

from katas.Finding_an_appointment import *

class TestFindingAnAppointment(unittest.TestCase):
    def test_parse_time_900(self):
        self.assertEqual(parse_time(900), '09:00')

    def test_parse_time_1000(self):
        self.assertEqual(parse_time(1000), '10:00')

    def test_parse_time_1215(self):
        self.assertEqual(parse_time(1215), '12:15')

    def test_parse_time_7800(self):
        with self.assertRaises(ValueError):
            parse_time(7800)

    def test_time_integer_simple(self):
        time = TimeInteger(900)
        time += 15
        self.assertEqual(time.value, 915)

    def test_time_integer_tricky(self):
        time = TimeInteger(900)
        time += 90
        self.assertEqual(time.value, 1030)

    def test_time_integer_tricky(self):
        time = TimeInteger(730)
        time += 87
        self.assertEqual(time.value, 857)

    def test_workinghours(self):
        working_hours = WorkingHours()
        for minute in working_hours:
            print(minute)
        self.assertTrue(False)


'''
schedules = [
  [['09:12', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
  [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
  [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]

test.assert_equals(get_start_time(schedules, 10), '09:00')



schedules = [
  [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']],
  [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
  [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
]
test.assert_equals(get_start_time(schedules, 60), '12:15')
test.assert_equals(get_start_time(schedules, 119), None)
test.assert_equals(get_start_time(schedules, 74), '12:15')
test.assert_equals(get_start_time(schedules, 76), None)
test.assert_equals(get_start_time(schedules, 80), None)
'''
