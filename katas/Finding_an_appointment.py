def parse_meeting(meeting):
    start_time = int(meeting[0].replace(':', ''))
    end_time =  int(meeting[1].replace(':', ''))
    return (start_time, end_time)


def parse_time(time):
    if time > 2400:
        raise ValueError
    if len(str(time)) == 3:
        time = '0' + str(time)
    str_time = str(time)[:2] + ':' + str(time)[2:]
    return str_time


class Person(object):
    def __init__(self):
        self.meetings = []

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
        time = 900
        current_time = TimeInteger(time)
        while current_time.value < 1900:
            current_time += 1
            print(current_time)
            yield current_time
        raise StopIteration

    def valid_working_hour(self, time):
        if time in set(self.hours) and int(str(time)[-2:]) < 60:
            return True
        return False


class NotGoodTime(Exception):
    pass


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

    def __eq__(self, integer):
        return self.value == integer



def get_start_time(schedules, duration):
    def check_time(time):
        for person in person_dictionary:
            current_person = person_dictionary[person]
            if current_person.is_busy_at(time):
                return False
        return True
    person_names= ['Annie', 'Bob', 'Candice', 'Danny', 'Esther', 'Ferenc', 'Gertrud']
    person_dictionary = {}
    for index, persons_schedule in enumerate(schedules):
        person_name = person_names[index]
        person_dictionary[person_name] = Person()
        for meeting in persons_schedule:
            person_dictionary[person_name].add_meeting(meeting)
    time_window_free = True
    for start_time in WorkingHours():
        if not start_time:
            continue
        if not time_window_free:
            new_free_window_starts_at = start_time
        try:
            time_window_free = True
            minute = 0
            while minute < duration:
                is_free_minute = check_time(start_time)
                if not is_free_minute:
                    time_window_free = False
                    raise NotGoodTime
                if not WorkingHours().valid_working_hour(start_time + minute):
                    raise NotGoodTime
                print(new_free_window_starts_at, minute)
                minute += 1
                if time_window_free and minute == duration:
                    return parse_time(new_free_window_starts_at)
        except NotGoodTime:
            continue
    return None
