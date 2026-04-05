import csv 

class Grade_Analyzer:
    def __init__(self, student_marks, student_count,failure_list, subject_count):
        self.student_marks = student_marks # This is our dictionary {Name: Total}
        self.student_count = student_count
        self.failure_list = failure_list
        self.subject_count = subject_count

    def generate_csv_report(self):
        #We use "Newline=''" to prevent blank rows in Excel
        with open("student_data_day_6.csv", "w", newline="", encoding="utf-8") as file:  # Open a file to write the average marks
            file.write("SCORE CARD📋:-\n")
            csv_writer = csv.writer(file)

            # 1. Write the Header (Top row of Your Spreadsheet)
            csv_writer.writerow(["Student name", "Total mark", "Average", "Status"])
            
            #2. Loop through your data and write rows
            for name, total in self.student_marks.items():
                average = total / len(self.subject_count)

                if average >= 80:
                    Status = "Excellent"
                elif 80 > average >= 40:
                    Status = "Average"                
                else:
                    Status = "Needs Attention"                

                csv_writer.writerow([name, total, f"{average:.2f}", Status])
    
    def generate_failure_report(self):
        with open("student_data_day_6.csv", "a", newline="", encoding="utf-8") as file:  # Open the same file to append the failure report
            csv_writer = csv.writer(file)
            # 1. Get the counts directly from your data
            fail_count = len(self.failure_list)
            pass_count = len(self.student_marks) - fail_count

            # 2. Write the Tracker Headers
            csv_writer.writerow([])  # Blank row for separation
            csv_writer.writerow(["FAILURE TRACKER 📉:-"])
            csv_writer.writerow([f"{pass_count} passes, {fail_count} failures"])

            # 3. Write each failure name and the subject they failed
            for name, reason in self.failure_list.items():
                csv_writer.writerow([name, reason])

    def toppers_list(self):
        with open("student_data_day_6.csv", "a", newline="", encoding="utf-8") as file:  # Open the same file to append the toppers list
            csv_writer = csv.writer(file)
            # 1. Sort students by average marks and get the top 3
            sorted_students = sorted(self.student_marks.items(), key=lambda x: x[1], reverse=True)
            top_students = sorted_students[:3]

            # 2. Write the Toppers Headers
            csv_writer.writerow([])  # Blank row for separation
            csv_writer.writerow(["TOPPERS LIST 🏆:-"])
            csv_writer.writerow(["Rank", "Student Name", "Total Marks"])

            # 3. Write each topper's name and total marks
            for rank, (name, total) in enumerate(top_students, start=1):
                if name in self.failure_list:
                    continue  # Skip students who failed
                csv_writer.writerow([rank, name, total])

#--- DATA INPUT SECTION ---
print("-------Day 6: CSV Data Architect WITH FAILURE TRACKING😍-------")

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
student_failure_list = {}

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
    while j < len(subject_list):
        try:
            mark = int(input(f"  Enter Mark for Subject {j+1}: "))
            
            # Simple Range Validation
            if 0 <= mark <= 100:
                if mark > 34:
                    total_mark += mark
                    j += 1  # Only move to the next subject if the input was a valid number
                else:
                    student_failure_list[name] = f"{mark} in {subject_list[j]}"
                    total_mark += mark
                    j += 1
            else:
                print("  ⚠️ Mark must be between 0 and 100.")
                
        except ValueError:
            print("  ⚠️ Invalid input! Please enter a numeric mark.")

    student_with_mark[name] = total_mark

# --- RUNNING THE ANALYZER ---
Analyzer = Grade_Analyzer(student_with_mark, student_count, student_failure_list, subject_list)
Analyzer.generate_csv_report()
Analyzer.generate_failure_report()
Analyzer.toppers_list()