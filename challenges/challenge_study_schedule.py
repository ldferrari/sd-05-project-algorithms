def study_schedule(start_time, end_time, target_time):

    students_on_target_time = 0
    for starting_at, finishing_at in zip(start_time, end_time):
        if (
            # starting_at == target_time
            # or finishing_at == target_time
            starting_at <= target_time <= finishing_at
        ):
            students_on_target_time += 1

    return students_on_target_time