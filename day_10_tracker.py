import numpy as np
import heapq


subjects_name = np.array(["Tamil", "English", "Maths", "Science", "Social"])
students_name = np.array(["Vijay", "Manoj", "Rahul", "ManickJamuna", "Mukilaa"])

# Pre-allocate an empty matrix (Rows = Students, Cols = Subjects)
# Using int16 just in case you want to sum them later (int8 max is 127)
students_marks = np.zeros((len(students_name), len(subjects_name)), dtype=np.int16)
student_total_mark = np.zeros((len(students_name)), dtype=np.int16)

for i in range(len(students_name)):
    print(f"\n--- Entering marks for {students_name[i]}🤗 ---")
    j = 0
    while j < len(subjects_name):
        try:
            mark_input = int(input(f"Enter marks for {subjects_name[j]}🫡: "))

            if 0 <= mark_input <= 100:
                students_marks[i, j] = mark_input
                student_total_mark[i] += mark_input
                j += 1  # Move to next subject only if input is valid
            else:
                print(" 🚨 Mark must be between 0 and 100!")

        except ValueError:
            print(" ⚠️ Invalid input! Please enter a whole number.")


# --- Displaying the Results ---
print("\n" + "=" * 30)
print("FINAL MARKSHEET📋")
print("=" * 30)

# Print Header
header = "Subjects".ljust(15) + "".join([s.center(10) for s in students_name])
print(header)

students_marks = students_marks.transpose()

# Print Rows
for idx, subj_name in enumerate(subjects_name):
    row_data = subj_name.ljust(15)
    for student_idx in range(len(students_name)):
        # Get the specific mark for THIS subject and THIS student
        mark = students_marks[idx, student_idx]
        row_data += str(mark).center(10)
    print(row_data)

print("\n" + "=" * 30)

print("Total marks".ljust(15) , end="")
for mark in student_total_mark:
    total_marks = f"{str(mark).center(10)}"
    print(total_marks, end="")
print("\n" + "=" * 30)



print("\nToppers 😍:-\n")
# Pair names and marks together first
rankings = list(zip(students_name, student_total_mark))
# Sort by the second item (the mark)
toppers = heapq.nlargest(3, rankings, key=lambda x: x[1])

for name, mark in toppers:
    print(f" {name}: {mark}")
print("\n" + "=" * 30)

 

