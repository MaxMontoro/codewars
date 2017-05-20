def parse_meeting(meeting):
    start_time = int(meeting[0].replace(':', ''))
    end_time =  int(meeting[1].replace(':', ''))
    return (start_time, end_time)


def parse_time(time):
    if len(str(time)) == 3:
        time = '0' + str(time)
    str_time = str(time)[:2] + ':' + str(time)[2:]
    return str_time


class Person(object):
    def __init__(self, name):
        self.meetings = []
        self.name = name

    def add_meeting(self, meeting):
        time = parse_meeting(meeting)
        self.meetings.append(time)

    def is_free_at(self, given_time):
        for meeting in self.meetings:
            if meeting[0] <= given_time and given_time < meeting[1]:
                return False
        return True

    def is_busy_at(self, given_time):
        return not self.is_free_at(given_time)


class WorkingHours(object):
    def __iter__(self):
        current_time = TimeInteger(900)
        while current_time.value < 1900:
            yield current_time.value
            current_time += 1

    @staticmethod
    def validate_working_hour(time):
        if 900  <= time <= 1900:
            return True
        return False


class TimeInteger(int):
    def __init__(self, value):
        self.value = value

    def __add__(self, other_value):
        for minute in range(other_value):
            if str(self.value)[-2:] == '59':
                hour = int(str(self.value)[:2]) if len(str(self.value)) == 4 else int(str(self.value)[0])
                hour += + 1
                self.value = hour * 100
            else:
                self.value += 1
        return self

    def __ge__(self, other):
        if isinstance(other, int):
            return self.value >= other
        else:
            return self.value >= other.value

    def __le__(self, other):
        if isinstance(other, int):
            return self.value <= other
        else:
            return self.value <= other.value


def get_start_time(schedules, duration):

    def check_time(time):
        for person in person_dictionary:
            if person_dictionary[person].is_busy_at(time):
                return False
        return True

    person_names= ['Annie', 'Bob', 'Candice', 'Danny', 'Esther', 'Ferenc', 'Gertrud']
    person_dictionary = {}

    def build_schedules(schedules):
        for index, persons_schedule in enumerate(schedules):
            person_dictionary[person_names[index]] = Person(person_names[index])
            for meeting in persons_schedule:
                person_dictionary[person_names[index]].add_meeting(meeting)

    build_schedules(schedules)

    time_window_free = True
    new_free_window_starts_at = 900

    for minute in WorkingHours():

        if not time_window_free:
            new_free_window_starts_at = minute

        time_window_free = True
        free_minutes_so_far = 0
        while free_minutes_so_far < duration:
            minute_to_check = TimeInteger(minute) + free_minutes_so_far
            is_free_minute = check_time(minute_to_check)

            if not is_free_minute:
                time_window_free = False
                break

            free_minutes_so_far += 1
            if time_window_free and free_minutes_so_far == duration:

                def validate_meeting_time(start, end):
                    return WorkingHours.validate_working_hour(start) and WorkingHours.validate_working_hour(end)

                meeting_start_time = new_free_window_starts_at
                meeting_end_time = TimeInteger(new_free_window_starts_at) + duration
                if validate_meeting_time(meeting_start_time, meeting_end_time):
                    return parse_time(new_free_window_starts_at)

    return None
