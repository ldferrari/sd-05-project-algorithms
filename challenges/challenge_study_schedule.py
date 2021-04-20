def study_schedule(start_time, end_time, target_time):
    """ Retorna número de estudantes ativos no target_time. """
    students = 0

    if (not start_time or not end_time):
        return 0

    for [i, s] in enumerate(start_time):
        if s <= target_time <= end_time[i]:
            students += 1

    return students
