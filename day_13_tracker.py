import xml.etree.ElementTree as ET

# 1. Create the root element
root = ET.Element("StudentProfile")

# 2. Add a child element (Name)
name = ET.SubElement(root, "Name")
name.text = "Manojkumar M"

# 3. Add a child element with an attribute (Course)
course = ET.SubElement(root, "Course", branch="AI & Data Science")
course.text = "B.Tech"

# 4. Wrap it in a tree and save it
tree = ET.ElementTree(root)

# Write to a file
tree.write("profile.xml", encoding="utf-8", xml_declaration=True)

# Just to show you the output in the terminal:
ET.dump(root)