import json
import os
import random
from gpa_calculator import CGPACalculator 

def get_safe_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input! Defaulting to 0.")
        return 0

def save_to_database(student_data, filename="records.json"):
    # 1. Initialize an empty list
    all_students = []

    # 2. READ: Pull existing students into Python memory
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as file:
            try:
                all_students = json.load(file)
            except json.JSONDecodeError:
                # If file is corrupted, start fresh
                all_students = []

    # 3. MODIFY: Add the new student to the Python list
    all_students.append(student_data)

    # 4. WRITE: Overwrite the file with the full, updated list
    # Using 'w' ensures the file is always a single, valid JSON array
    try:
        with open(filename, "w") as file:
            json.dump(all_students, file, indent=4)
        print(f"\n✅ Success: {student_data['name']} added to {filename}")
        print(f"📊 Total Students in file: {len(all_students)}")
    except IOError as e:
        print(f"❌ File Error: {e}")

def main():
    print("--- Day 11: AI Student Record System ---")
    
    # 1. Setup Data
    grade_points = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C+': 5, 'C': 4, 'U': 0}
    
    # Get user input for today's entry
    try:
        name = input("Enter Student Name: ")
        if not name.strip():
            print("Name cannot be empty.")
            return
        elif name.isdigit():
            print("Name cannot be a number.")
            return
        elif any(char.isdigit() for char in name):
            print("Name cannot contain numbers.")
            return
        elif len(name) > 20 or len(name) < 2:
            print("Name is not within the allowed length (2-20 characters). Please enter a name with 20 characters or fewer.")
            return
        else:
            pass  # Name is valid, continue with the program
    except Exception:
        print("Invalid input. Please enter a valid name.")
        return

    try:
        num_subjects = int(input("Enter number of subjects: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Generate random credits (1-4) and get marks
    credits = [random.randint(2, 4) for _ in range(num_subjects)]
    subjects = [input(f"Enter subject {i+1}: ") for i in range(num_subjects)]
    marks = [get_safe_input(f"Enter marks for subject {i+1}: ") for i in range(num_subjects)]
    
    # 2. Use the imported Logic
    calc = CGPACalculator(grade_points, credits, marks)
    cgpa_result = calc.get_cgpa() # Using the 'get_cgpa' method we discussed
    
    # 3. Create the JSON-ready Dictionary
    current_entry = {
        "name": name,
        "marks": marks,
        "subjects": subjects,
        "final_cgpa": round(cgpa_result, 2)
    }
    
    # 4. Save to the file
    save_to_database(current_entry)
    
    print(f"Processed CGPA: {cgpa_result:.2f}")
    print("Check your folder for 'records.json' to see the permanent data!")

if __name__ == "__main__":
    main()