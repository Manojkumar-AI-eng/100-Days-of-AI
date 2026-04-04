import csv #🏃‍♀️‍➡️New Tool For Day 5

class Grade_Analyzer:
    def __init__(self, student_marks, subject_count):
        self.student_marks = student_marks # This is our dictionary {Name: Total}
        self.subject_count = subject_count

    def generate_csv_report(self):
        #We use "Newline=''" to prevent blank rows in Excel
        with open("student_data_day_5.csv", "w", newline="") as file:  # Open a file to write the average marks
            file.write("SCORE CARD📋:-\n")
            csv_writer = csv.writer(file)

            # 1. Write the Header (Top row of Your Spreadsheet)
            csv_writer.writerow(["Student name", "Total mark", "Average", "Status"])
            
            #2. Loop through your data and write rows
            for name, total in self.student_marks.items():
                average = total / self.subject_count

                if average >= 80:
                    Status = "Excellent"
                elif 80 > average >= 40:
                    Status = "Average"                
                else:
                    Status = "Needs Attention"                

                csv_writer.writerow([name, total, f"{average:.2f}", Status])
        
        print("\n✅ Success! 'student_data_day5.csv' has been created😎")
#--- DATA INPUT SECTION ---
print("-------Day 5: CSV Data Architect😍-------")

# 1. Validation for subject and student counts
while True:
    try:
        subject_count = int(input("How many subjects do u have?🤔 : "))
        student_count = int(input("How many students want to analyze?🤔 : "))
        
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

# --- RUNNING THE ANALYZER ---
Analyzer = Grade_Analyzer(student_with_mark, student_count)
Analyzer.generate_csv_report()