# Manojkumar's 100-Day AI Roadmap
# Target: Job-Ready by July 2026

phases = {
    "Phase 1: Python Master and Data Analytics (Pandas/NumPy)": range(1, 31),
    "Phase 2: Data Structure": range(31, 61),
    "Phase 3: Machine Learning (Scikit-Learn)": range(61, 91),
    "Phase 4: Capstone Project & Portfolio": range(91, 101)
}

print(f"🚀 STARTING 100 DAYS OF AI & DATA SCIENCE\n" + "="*40)

for phase_name, days in phases.items():
    print(f"\n📍 {phase_name}")
    print(f"   Days: {days.start} to {days.stop - 1}")
    
    if "Python" in phase_name:
        print("   Goal: Master OOP and Clean messy data and build charts.")
    elif "Data Structure" in phase_name:
        print("   Goal: Master Data Structures.")
    elif "Machine Learning" in phase_name:
        print("   Goal: Build your first prediction models.")
    else:
        print("   Goal: Finish a project for My Resume!")

print("\n" + "="*40 + "\n🔥 1% better every day. Let's go!")
