import numpy as np

# 1. THE GRID: Create a 3x3 matrix (like a small digital image or a database)
# Instead of 9 lines of code, we use 1.
data = np.array([[10, 20, 30], 
                 [40, 50, 60], 
                 [70, 80, 90]])

# 2. THE SUPERPOWER: Add 5 to every single number at once (Broadcasting)
# In basic Python, this would need a nested 'for' loop.
boosted_data = data + 5

# 3. THE FILTER: Find only the numbers greater than 50
# This is how we scan for "Threats" in Security or "High Scores" in AI.
high_values = data[data > 50]

print("Original Grid:\n", data)
print("\nEvery element + 5:\n", boosted_data)
print("\nValues greater than 50:", high_values)