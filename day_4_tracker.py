class Grade_Analyzer:
    def __init__(self, student_marks, subject_count):
        self.student_marks = student_marks # This is our dictionary {Name: Total}
        self.subject_count = subject_count

    def calculate_average(self):
        # Instead of self.keys and self.values, we use .items()
        # .items() gives us both the Key (Name) and Value (Total) at once
        with open("average_marks.txt", "w", newline="") as file:  # Open a file to write the average marks
            file.write("Average Marks of Students/Student:\n")
            for name, total in self.student_marks.items():
                average = total / self.subject_count
                file.write(f"{name}: {average:.2f}\n")

                if average >= 80:
                    file.write("Status: Excellent\n\n")
                elif 80 > average >= 40:
                    file.write("Status: Average\n\n")
                else:
                    file.write("Status: Needs Attention\n\n")
                print(f"{name}: {average:.2f}\n")

print("-------Data Asker-------")

# 1. Validation for subject and student counts
while True:
    try:
        subject_count = int(input("How many subjects do u have? : "))
        student_count = int(input("How many students want to analyze? : "))
        
        # Check if the numbers are actually useful (Greater than 0)
        if subject_count > 0 and student_count > 0:
            break 
        else:
            print("❌ Error: You must have at least 1 subject and 1 student!")
            
    except ValueError:
        print("❌ Error: Please enter a whole number (e.g., 5).")

student_with_mark = {}

for i in range(student_count):
    while True:
        name = input(f"Enter Student Name {i+1} : ").strip() # .strip() removes extra spaces
        
        # Check if the name is empty or is just a number
        if not name:
            print("  ⚠️ Name cannot be empty!")
        elif name.isnumeric():
            print("  ⚠️ A name cannot be just a number. Please enter a real name.")
        else:
            break # Name is valid text!
            
    total_mark = 0
    
    j = 0
    while j < subject_count:
        try:
            mark = int(input(f"  Enter Mark for Subject {j+1}: "))
            
            # Simple Range Validation
            if 0 <= mark <= 100:
                total_mark += mark
                j += 1  # Only move to the next subject if the input was a valid number
            else:
                print("  ⚠️ Mark must be between 0 and 100.")
                
        except ValueError:
            print("  ⚠️ Invalid input! Please enter a numeric mark.")

    student_with_mark[name] = total_mark

cls_name = Grade_Analyzer(student_with_mark, student_count)
cls_name.calculate_average() 
