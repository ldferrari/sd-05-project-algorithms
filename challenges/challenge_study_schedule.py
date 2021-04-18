def study_schedule(start_time, end_time, target_time):
    contador = 0
    if start_time == "" or end_time == "":
        return contador

    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            contador += 1

    return contador
