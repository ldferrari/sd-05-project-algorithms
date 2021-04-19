def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    count_studing = 0
    for i in range(len(start_time)):
        if end_time[i] >= target_time >= start_time[i]:
            count_studing += 1

    return count_studing
