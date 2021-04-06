import persons

best_student = persons.Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

the_best_student = persons.Student('Billy', 'Herrington', 'GAY')
the_best_student.courses_in_progress += ['Python']


cool_reviewer = persons.Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = persons.Lecturer('Jotaro', 'Kujo')
cooler_lecturer = persons.Lecturer('Jonatan', 'Jostar')

cool_lecturer.courses_attached += ['Python']
cooler_lecturer.courses_attached += ['Python']


best_student.rate_lector(cool_lecturer, 'Python', 9)
best_student.rate_lector(cool_lecturer, 'Python', 5)
best_student.rate_lector(cool_lecturer, 'Python', 10)

best_student.rate_lector(cooler_lecturer, 'Python', 10)
best_student.rate_lector(cooler_lecturer, 'Python', 10)
best_student.rate_lector(cooler_lecturer, 'Python', 10)
best_student.rate_lector(cooler_lecturer, 'Python', 10)


cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

cool_reviewer.rate_hw(the_best_student, 'Python', 10)
cool_reviewer.rate_hw(the_best_student, 'Python', 10)
cool_reviewer.rate_hw(the_best_student, 'Python', 10)


print(persons.mid_rate(the_best_student))
print(persons.get_avarage(persons.get_list_students()))
print(persons.get_avarage(persons.get_list_lectors()))
print(the_best_student.dfinished_courses())
print(the_best_student.dcourses_in_progress())
print(the_best_student)
print(the_best_student > best_student)
print(the_best_student >= best_student)
print(the_best_student == best_student)
print(cooler_lecturer)
print(cool_lecturer < cooler_lecturer)
print(cool_lecturer >= cooler_lecturer)
print(cool_lecturer == cooler_lecturer)

