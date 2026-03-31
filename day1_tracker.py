my_profile = {
    "name": "Manojkumar M",
    "role": "AI Student",
    "skills": ["Python", "Machine Learning", "Data Analysis"],
    "daily_tasks": ["Coding", "Learning new concepts", "Building projects"],
    "daily_streak": 1
}

print(f'---welcome to day [{my_profile["daily_streak"]}] ---')
print(f'Name: {my_profile["name"]}')

print("\nSkills to master this year:")
for skill in my_profile["skills"]:
    print(f"- {skill}")