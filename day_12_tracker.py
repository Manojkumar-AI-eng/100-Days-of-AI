import json
import os

# Create a folder for report cards if it doesn't exist
output_folder = "Student_Reports"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

filename = "Outputs For the Codes/records.json"

# Load data safely
if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, "r") as f:
        data = json.load(f)
else:
    data = []

# Generate Report Cards
for record in data:
    # Save inside the 'Student_Reports' folder
    file_path = os.path.join(output_folder, f"{record['name']}_Report.txt")
    
    with open(file_path, "w") as f:
        f.write(f"OFFICIAL REPORT CARD: {record['name']}\n")
        f.write("=" * 40 + "\n\n")
        
        f.write("Subject-wise Marks:\n")
        # Use zip to pair subjects with marks!
        for subject, mark in zip(record['subjects'], record['marks']):
            f.write(f"  - {subject.ljust(15)}: {mark}\n")
            
        f.write("\n" + "-" * 40 + "\n")
        f.write(f"FINAL CALCULATED CGPA: {record['final_cgpa']}\n")
        f.write("-" * 40 + "\n")

print(f"Done! Check the '{output_folder}' folder for results.")