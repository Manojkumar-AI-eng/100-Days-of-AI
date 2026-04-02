# This program calculates the average marks of students based on the total marks and the number of subjects.

class Grade_Analyzer:
    def __init__(self, student_marks, subject_count):
        self.student_marks = student_marks # This is our dictionary {Name: Total}
        self.subject_count = subject_count

    def calculate_average(self):
        # Instead of self.keys and self.values, we use .items()
        # .items() gives us both the Key (Name) and Value (Total) at once
        for name, total in self.student_marks.items():
            average = total / self.subject_count
            print(f"{name}: {average:.2f}")

print("-------Data Asker-------")

subject_count = int(input("How many subjects do u have? : "))
student_count = int(input("How many students want to analyze? : "))

student_with_mark = {}

for i in range(student_count):
    name = input(f"Enter Student Name {i+1} : ")
    total_mark = 0
    for j in range(subject_count):
        mark = int(input(f"Enter Mark {j+1}: "))
        total_mark += mark
    
    student_with_mark[name] = total_mark

# Create the object
analyzer = Grade_Analyzer(student_with_mark, subject_count)

print("\n-------Average Marks---------")
analyzer.calculate_average()