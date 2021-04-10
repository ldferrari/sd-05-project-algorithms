def study_schedule(start_time, end_time, target_time=0):
    if target_time == 0:
        return target_time
    count = 0
    i = 0
    while i < len(start_time):
        if end_time[i] >= target_time >= start_time[i]:
            count += 1
        i += 1
    return count
