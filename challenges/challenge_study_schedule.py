def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    online_students = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            online_students += 1
    return online_students
