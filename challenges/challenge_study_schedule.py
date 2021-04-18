def study_schedule(start_time=[], end_time=[], target_time=None):
    """ Faça o código aqui. """
    count = 0
    if not target_time or not start_time or not end_time:
        return 0
    for idx in range(len(start_time)):
        if start_time[idx] <= target_time <= end_time[idx]:
            count += 1
    return count
