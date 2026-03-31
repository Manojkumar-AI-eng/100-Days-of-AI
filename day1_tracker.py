# CGPA Calculator

import random

class CGPACalculator:
    def __init__(self, grade_points, credits, marks):
        self.grade_points = grade_points
        self.credits = credits
        self.marks = marks

    def calculate_grade(self, total_weighted_points):
        total_weighted_points = 0

        for i in range(len(self.marks)):
            if self.marks[i] >= 90 and self.marks[i] <= 100:
                total_weighted_points += self.credits[i] * self.grade_points['O']

            elif self.marks[i] >= 85 and self.marks[i] < 90:
                total_weighted_points += self.credits[i] * self.grade_points['A+']

            elif self.marks[i] >= 80 and self.marks[i] < 85:
                total_weighted_points += self.credits[i] * self.grade_points['A']

            elif self.marks[i] >= 75 and self.marks[i] < 80:
                total_weighted_points += self.credits[i] * self.grade_points['B+']

            elif self.marks[i] >= 70 and self.marks[i] < 75:
                total_weighted_points += self.credits[i] * self.grade_points['B']

            elif self.marks[i] >= 60 and self.marks[i] < 70:
                total_weighted_points += self.credits[i] * self.grade_points['C+']

            elif self.marks[i] >= 50 and self.marks[i] < 60:
                total_weighted_points += self.credits[i] * self.grade_points['C']
            else:
                total_weighted_points += self.credits[i] * self.grade_points['U']

    def calculate_cgpa(self):
        cgpa = 0
        total_weighted_points = self.calculate_grade()
        total_credits = sum(self.credits)

        if total_weighted_points > 0 and total_credits > 0:
            cgpa = total_weighted_points / total_credits
            print(f"Your CGPA is: {cgpa:.2f}")
            
        else:
            if total_weighted_points == 0 or total_credits == 0:
                print("Error: Total weighted points and total credits must be greater than zero.")
            else:
                print("Error: Total weighted points and total credits must be positive numbers.")


grade_points = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C+': 5, 'C': 4, 'U': 0}

subjects = int(input("Enter the number of subjects: "))

credits = [random.randint(1,  a) for a in range(1, subjects+1) ]

print("Credits for each subject:", credits)

marks = [int(input(f"Enter marks for subject {x + 1}: ")) for x in range(0, subjects)]


calculator = CGPACalculator(grade_points, credits, marks)
calculator.calculate_cgpa()