# "Escrever algoritmo de, no máximo, complexidade O(n)"
#  (execution time proportional to input size)


def study_schedule(start_time, end_time, target_time):
    """ Faça o código aqui. """
    # 1. Prep variable that will stock ultimate result
    repeated = 0
    # 2. Take care of conditions from exercise requirements
    if (start_time == [] or end_time == []):
        return repeated
    # 3. Iterate through each index corresponding with each student
    # and count how many times the target_time is within studying time slot
    for i in range(len(start_time)):
        # range starts with 0, so for i 0, 1,...until end of start_time array
        # (or end_time, does not matter, same length)
        if start_time[i] <= target_time <= end_time[i]:
            repeated += 1
    return repeated
    # (naturally will return 0 if target_time is always out of every time slot)


# 4. Testar function
start_time = [4, 1, 3, 2]
end_time = [4, 3, 4, 5]
print(study_schedule(start_time, end_time, 3))
# ``python challenges/challenge_study_schedule.py`` successfully returns 3
