def study_schedule(start_time, end_time, target_time):
    output = 0
    for i, student_start_time in enumerate(start_time):
        if student_start_time <= target_time and end_time[i] >= target_time:
            output += 1
    return output
