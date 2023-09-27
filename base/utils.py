import jdatetime


def split_persian_date(date):
    year = int(date.split('-')[0])
    month = int(date.split('-')[1])
    day = int(date.split('-')[2])

    return year, month, day


def is_member(user):
    return user.groups.filter(name='کاربر فنی').exists()


def to_gregorian(date):
    try:
        year, month, day = date.split('-')
        date = jdatetime.date(int(year), int(month), int(day)).togregorian()
        return date
    except (ValueError, AttributeError):
        # in case that one of start date or end date is empty
        return None


def full_name_extractor(name):
    if name:
        return name.split(' ')
    else:
        # in case the executor name does not provided
        # return firstname and lastname as none
        return None, None


def total_seconds_calculator(task, total_seconds):
    t_start = task.start_time
    t_end = task.end_time
    seconds_start = (t_start.hour * 60 + t_start.minute) * 60 + t_start.second
    seconds_end = (t_end.hour * 60 + t_end.minute) * 60 + t_end.second
    total_seconds += seconds_end - seconds_start
    return total_seconds


def find_longest_work(task, the_longest_work_seconds, the_longest_work_object):
    t_start = task.start_time
    t_end = task.end_time
    seconds_start = (t_start.hour * 60 + t_start.minute) * 60 + t_start.second
    seconds_end = (t_end.hour * 60 + t_end.minute) * 60 + t_end.second
    current_task_seconds = seconds_end - seconds_start
    if the_longest_work_seconds <= current_task_seconds:
        the_longest_work_object = task
        # return max(the_longest_work_seconds, current_task_seconds), the_longest_work
    return max(the_longest_work_seconds, current_task_seconds), the_longest_work_object
