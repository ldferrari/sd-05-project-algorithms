def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    online = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            online += 1
    return online