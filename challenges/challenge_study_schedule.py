def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    if len(start_time) == 0:
        return 0
    if target_time == 0:
        return 0
    counter = 0
    for s, e in zip(start_time, end_time):
        if s <= target_time <= e:
            counter += 1

    return counter
