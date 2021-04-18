def study_schedule(start_time, end_time, target_time):
    if len(start_time) == 0 or len(end_time) == 0:
        return 0
    counter = 0
    for index, item in enumerate(end_time):
        if (start_time[index] <= target_time <= item):
            counter += 1
    return counter
