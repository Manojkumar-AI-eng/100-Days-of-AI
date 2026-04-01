# Automated student Grade Analyzer

class Grade_analyzer:
    def __init__(self, no_of_marks):
        self.no_of_marks = no_of_marks
        self.average_mark = 0

    def calculate_average(self):
        marks = []
        while len(marks) < self.no_of_marks:
            try:
                a = int(input(f"Enter Mark for the subject no.{len(marks) + 1}:"))
                if 0 < a <= 100:
                    marks.append(a)
                else:
                    print("Enter a valid Mark between 0 and 100!")
            except ValueError:
                print("Please enter a number for the subject")

        self.average_mark = sum(marks) / len(marks) #Formula for average
        print(f"\nYour Average is : {self.average_mark:.2f}")
        return self.average_mark

    def display_category(self):

        if 80 <= self.average_mark <= 100:
            print("Status: Excellent")

        elif 80 > self.average_mark >= 40:
            print("Status: Average")

        else:
            print("Status: Needs Attention")


#----------Execution----------
try:
    counter = int(input("How many subjects do u have?"))
    if counter > 0:
        cls_name = Grade_analyzer(counter)

        cls_name.calculate_average()
        cls_name.display_category()

    else:
        print(".........You need at least one subject.........")

except ValueError:
    print("Please enter a number for the subject count!")