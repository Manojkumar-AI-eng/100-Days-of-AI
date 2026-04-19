import xml.etree.ElementTree as ET

class Result: # Class names should be Capitalized in Python (PEP 8)
    def __init__(self, student_and_mark, total_marks):
        self.student_and_mark = student_and_mark
        self.total_marks = total_marks

    def generate_xml_report(self, subjects):
        # Create the root element
        root = ET.Element("StudentProfile")

        # Iterate through student data
        for indx, (student_name, marks) in enumerate(self.student_and_mark.items()):
            # Create a student container
            std_node = ET.SubElement(root, f"Student_{indx + 1}")

            name_elem = ET.SubElement(std_node, "Name")
            name_elem.text = str(student_name)

            # Add marks
            mark_list = ET.SubElement(std_node, "Marks")
            for sub, mark in zip(subjects, marks):
                sub_elem = ET.SubElement(mark_list, sub.replace(" ", "_")) # Tags can't have spaces
                sub_elem.text = str(mark)

            # Add total
            total_elem = ET.SubElement(mark_list, "Total")
            total_elem.text = str(self.total_marks[student_name])
 
        # Correct way to save XML in Python
        tree = ET.ElementTree(root)
        ET.indent(tree, space="  ") # Makes the XML look pretty!
        tree.write("Student_marks_in_xml.xml", encoding="utf-8", xml_declaration=True)
        print("\n✅ Report Generated: Student_marks_in_xml.xml")

# --- DATA INPUT SECTION ---
while True:
    try:
        sub_count = int(input("How many subjects do you have?: "))
        subject_list = [input(f"  Enter Subject Name {i+1} : ").strip() for i in range(sub_count)]
        student_count = int(input("How many students to analyze? 🤔 : "))
        
        if len(subject_list) > 0 and student_count > 0:
            break 
        print("❌ Error: Minimum 1 subject and 1 student required!")
    except ValueError:
        print("❌ Error: Please enter a whole number.")

student_mark_details = {} # Stores list of marks
student_totals = {}       # Stores total sums

for i in range(student_count):
    while True:
        name = input(f"\nEnter Student Name {i+1} : ").strip()
        if name and not name.isdigit():
            break
        print("⚠️ Please enter a valid name.")
            
    temp_marks = []
    j = 0
    while j < len(subject_list):
        try:
            m = int(input(f"  Enter Mark for {subject_list[j]}: "))
            if 0 <= m <= 100:
                temp_marks.append(m)
                j += 1
            else:
                print("⚠️ Mark must be 0-100.")
        except ValueError:
            print("⚠️ Enter a numeric value.")

    student_mark_details[name] = temp_marks
    student_totals[name] = sum(temp_marks)

# --- RUNNING THE ANALYZER ---
analyzer = Result(student_mark_details, student_totals)
analyzer.generate_xml_report(subject_list)