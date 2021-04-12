def study_schedule(start_time, end_time, target_time):
    studing = 0
    students = len(start_time)
    for student in range(students):
        if start_time[student] <= target_time <= end_time[student]:
            studing += 1
    return studing
