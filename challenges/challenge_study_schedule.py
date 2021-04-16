def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    student = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time and end_time[index] >= target_time:
            student += 1

    return student
