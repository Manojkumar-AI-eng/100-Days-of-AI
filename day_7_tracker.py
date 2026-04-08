import csv

class Grade_Analyzer:
    def __init__(self, student_marks_dict, student_mark_list):
        self.student_marks_dict = student_marks_dict # {Name: Total}
        self.student_mark_list = student_mark_list   # {Name: [Marks]}

    def generate_csv_report(self, subjects):
        for name, total in self.student_marks_dict.items():
            # This creates the file!
            with open(f"{name}.csv", "w", newline="", encoding="utf-8") as file:
                file.write("SCORE CARD📋:-\n")
                csv_writer = csv.writer(file)
                csv_writer.writerow([])
                csv_writer.writerow([f"Student Name : {name}"])
                csv_writer.writerow(["Subject name", "Mark(s)", "Status"])

                # Get marks for this specific student
                marks = self.student_mark_list[name]
                
                csv_writer.writerow([])
                for sub, mar in zip(subjects, marks):
                    status = "Pass" if mar > 34 else "Fail"
                    csv_writer.writerow([sub, mar, status])

                csv_writer.writerow([])
                csv_writer.writerow([f"Total : {total}"])
        print("✅ Reports generated successfully!")
    
    
#--- DATA INPUT SECTION ---
print("-------Day 7: CSV Data Architect For Every Single Student Score Card😍-------")

# 1. Validation for subject and student counts
while True:
    try:
        subject_list = [input(f"  Enter Subject Name {i+1} :").strip() for i in range(int(input("How many subjects do you have?:")))]
        student_count = int(input("How many students want to analyze?🤔 : "))
        
        # Check if the numbers are actually useful (Greater than 0)
        if len(subject_list) > 0 and student_count > 0:
            break 
        else:
            print("❌ Error: You must have at least 1 subject and 1 student!")
            
    except ValueError:
        print("❌ Error: Please enter a whole number (e.g., 5).")

student_with_mark = {}
student_mark_list = {}

for i in range(student_count):
    while True:
        name = str(input(f"Enter Student Name {i+1} : ").strip()) # .strip() removes extra spaces
        
        # Check if the name is empty or is just a number
        if not name:
            print("  ⚠️ Name cannot be empty!")
        elif name.isnumeric():
            print("  ⚠️ A name cannot be just a number. Please enter a real name.")
        elif name.isalnum():
            print("  ⚠️ Name doesn't contain Numbers!")
        else:
            break #name is a valid NAME
            
    total_mark = 0
    temp_mark = []
    
    j = 0
    while j < len(subject_list):
        try:
            mark = int(input(f"  Enter Mark for Subject {j+1}: "))
            
            if not mark:
                print("  ⚠️ Mark cannot be empty")
            elif 100 >= mark >= 0:
               total_mark += mark
               temp_mark.append(mark)
               j+=1
            else:
                print("  ⚠️ Mark must be between 0 and 100.")
                
        except ValueError:
            print("  ⚠️ Invalid input! Please enter a numeric mark.")

    student_with_mark[name] = total_mark
    student_mark_list[name] = temp_mark

# --- RUNNING THE ANALYZER ---
Analyzer = Grade_Analyzer(student_with_mark, student_mark_list)
Analyzer.generate_csv_report(subject_list) # Pass the subjects here