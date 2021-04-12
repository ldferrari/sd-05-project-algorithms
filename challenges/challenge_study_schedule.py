def study_schedule(start_time, end_time, target_time):
    result = 0
    if (start_time == [] or end_time == []):
        return 0
    for index, item in enumerate(end_time):
        if (start_time[index] <= target_time <= item):
            result += 1
    return result


start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]
print(study_schedule(start_time, end_time, 3))
