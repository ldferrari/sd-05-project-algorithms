def study_schedule(start_time, end_time, target_time):
    counter = 0
    if start_time == [] or target_time == 0:
        return 0
    for index in range(len(end_time)):
        if target_time <= end_time[index]:
            if start_time[index] <= target_time:
                counter += 1

    return counter