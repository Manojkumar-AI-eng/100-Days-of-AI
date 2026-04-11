import random

class CGPACalculator:
    def __init__(self, grade_points, credits, marks):
        self.grade_points = grade_points
        self.credits = credits
        self.marks = marks

    def calculate_grade(self):
        total_weighted_points = 0
        for i in range(len(self.marks)):
            m = self.marks[i]
            if m >= 90: gp = self.grade_points['O']
            elif m >= 85: gp = self.grade_points['A+']
            elif m >= 80: gp = self.grade_points['A']
            elif m >= 75: gp = self.grade_points['B+']
            elif m >= 70: gp = self.grade_points['B']
            elif m >= 60: gp = self.grade_points['C+']
            elif m >= 50: gp = self.grade_points['C']
            else: gp = self.grade_points['U']
            
            total_weighted_points += self.credits[i] * gp
        return total_weighted_points

    def get_cgpa(self):
        """Returns the CGPA value instead of just printing it."""
        total_weighted_points = self.calculate_grade()
        total_credits = sum(self.credits)
        
        if total_credits > 0:
            return total_weighted_points / total_credits
        return 0.0

# This block prevents the code below from running when you import it into Day 11
if __name__ == "__main__":
    grade_points = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C+': 5, 'C': 4, 'U': 0}
    subjects = int(input("Enter the number of subjects: "))
    credits = [random.randint(1, 4) for _ in range(subjects)]
    marks = [int(input(f"Enter marks for subject {x + 1}: ")) for x in range(subjects)]

    calculator = CGPACalculator(grade_points, credits, marks)
    result = calculator.get_cgpa()
    print(f"Your CGPA is: {result:.2f}")