def study_schedule(start_time, end_time, target_time):
    if start_time == [] or end_time == []:
        return 0

    counter = 0

    for i, elem in enumerate(end_time):
        if elem < start_time[i]:
            raise ValueError('the end time should occur after the start time')
        if start_time[i] <= target_time <= elem:
            counter += 1  
    return counter
