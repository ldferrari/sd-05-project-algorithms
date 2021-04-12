def study_schedule(start_time, end_time, target_time):
    if start_time == "" or end_time == "":
        return 0

    saida = 0

    for index in range(len(start_time)):
        if start_time[index] <= target_time and end_time[index] >= target_time:
            saida += 1

    return saida

# print(study_schedule([4, 1, 3, 2], [4, 3, 4, 5], 3))
