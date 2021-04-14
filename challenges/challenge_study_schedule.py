def study_schedule(start_time, end_time, target_time):
    count = 0

    if start_time == "" or end_time == "":
        return count

    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            count += 1

    return count
