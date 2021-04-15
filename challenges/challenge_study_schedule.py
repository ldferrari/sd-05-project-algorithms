def study_schedule(start_time, end_time, target_time):
    if start_time == "" or end_time == "":
        return 0

    contador = 0

    for index in range(len(start_time)):
        if start_time[index] <= target_time >= end_time[index]:
            contador += 1
    return contador
