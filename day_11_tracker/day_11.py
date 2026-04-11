import json
import os
import random
from gpa_calculator import CGPACalculator 

def save_to_database(student_data, filename="records.json"):
    """
    Handles the 'Load -> Update -> Save' logic for our JSON database.
    """
    try:
        # 1. Load existing data (The 'Security Guard' check)
        if os.path.exists(filename):
            with open(filename, "r") as file:
                database = json.load(file)
        else:
            database = []

        # 2. Add the new record to our list
        database.append(student_data)

        # 3. Write the updated list back to the file (The 'Freezer')
        with open(filename, "w") as file:
            json.dump(database, file, indent=4)
            
        print(f"\n✅ Success: Record persisted to {filename}")
        
    except IOError as e:
        print(f"❌ File Error: {e}")

def main():
    print("--- Day 11: AI Student Record System ---")
    
    # 1. Setup Data
    grade_points = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C+': 5, 'C': 4, 'U': 0}
    
    # Get user input for today's entry
    name = input("Enter Student Name: ")
    num_subjects = int(input("Enter number of subjects: "))
    
    # Generate random credits (1-4) and get marks
    credits = [random.randint(2, 4) for _ in range(num_subjects)]
    marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(num_subjects)]
    
    # 2. Use the imported Logic
    calc = CGPACalculator(grade_points, credits, marks)
    cgpa_result = calc.get_cgpa() # Using the 'get_cgpa' method we discussed
    
    # 3. Create the JSON-ready Dictionary
    current_entry = {
        "day": 11,
        "name": name,
        "marks": marks,
        "credits": credits,
        "final_cgpa": round(cgpa_result, 2),
        "tools_used": ["json", "os", "OOP"]
    }
    
    # 4. Save to the file
    save_to_database(current_entry)
    
    print(f"Processed CGPA: {cgpa_result:.2f}")
    print("Check your folder for 'records.json' to see the permanent data!")

if __name__ == "__main__":
    main()