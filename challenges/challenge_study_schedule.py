def study_schedule(start_time, end_time, target_time):
    estudante = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time and end_time[index] >= target_time:
            estudante += 1

    return estudante
