num_of_courses = int(input("How many courses did you finish? "))

course_marks = []

course_count = 1

while (course_count <= num_of_courses):
    course_marks.append(
        int(input(f"Enter your mark for course {course_count}: ")))
    course_count += 1

for item in course_marks:
    print(item)

total = 0
for mark in course_marks:
    total += mark  # total = total + mark

# Another way from other students: (longer but good example of using range()):
"""
for i in range(len(course_marks)):
    # starting form [0] to [length of (course_marks) - 1]
    # i=0, i=1, i=2, .... i=x,
    total += course_marks[i]

# for testing:
print(total)

Or:
for i in range(num_of_courses):
    total += course_marks[i]
"""

average = round(total/num_of_courses, 2)

print(f"Your average for your {num_of_courses} courses is: {average}")

if average >= 90 and average <= 100:
    print("Your grade is A+")
elif average >= 80 and average <= 89:
    print("Your grade is B")
elif average >= 70 and average <= 79:
    print("Your grade is C")
elif average >= 60 and average <= 69:
    print("Your grade is D")
elif average <= 60:
    print("Your grade is F")
