def study_schedule(start_time, end_time, target_time):
    if (not (start_time and end_time and target_time)):
        return 0

    contador = 0

    for i in range(len(start_time)):
        hours = list(range(start_time[i], end_time[i]+1))
        if target_time in hours:
            contador += 1
    return contador
