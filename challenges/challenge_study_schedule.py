def study_schedule(start_time, end_time, target_time):
    if len(start_time) == 0 or len(end_time) == 0 or target_time == 0:
        return 0

    # print(f'start {start_time}, {end_time}')
    times = [0] * 7
    for index in range(0, len(start_time)):
        time_in = start_time[index]
        time_out = end_time[index]
        times[time_in] += 1
        times[time_out+1] -= 1

    total = 0
    for index in range(1, target_time + 1):
        total += times[index]

    return total


# start_time = [4, 1, 3, 2]
# end_time = [4, 3, 4, 5]
# print(study_schedule(start_time, end_time, 5))
    # index         0  1  2  3  4  5
    # estudante     1  2  3  4  5  6
    # start_time = [2, 1, 2, 1, 4, 4]
    # end_time   = [2, 2, 3, 5, 5, 5]

    # horas           0  1  2   3   4   5   6
    # times          [0, 0, 1, -1,  0,  0,  0] index 0
    # times          [0, 1, 1, -2,  0,  0,  0] index 1
    # times          [0, 1, 2, -2, -1,  0,  0] index 2
    # times          [0, 2, 2, -2, -1,  0, -1] index 3
    # times          [0, 2, 2, -2,  0,  0, -2] index 4
    # times          [0, 2, 2, -2,  1,  0, -3] index 5
