#!/usr/bin/env python3

# Grade generator script
import csv

def main():
    assignments = []

    print("Enter assignment names")
    while True:
        # Input assignment name, stop if empty
        name = input("\nAssignment name (or press Enter to finish): ").strip()
        if name == "":
            break

        # Category validation
        category = input("Category (FA/SA): ").upper()
        while category not in ['FA', 'SA']:
            print("Invalid category. Please enter 'FA' for Formative Assessment or 'SA' for Summative Assessment.")
            category = input("Category (FA/SA): ").upper()

        # Grade validation
        while True:
            try:
                grade = float(input("Input your grade between 0-100: "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Invalid grade. Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        # Weight validation
        while True:
            try:
                weight = float(input("Input the weight (positive number): "))
                if weight > 0:
                    break
                else:
                    print("Weight must be positive.")
            except ValueError:
                print("Invalid input! Please enter a number.")

        # Store assignment details
        assignments.append({
            'name': name,
            'category': category,
            'grade': grade,
            'weight': weight
        })

        # Check if the user wants to add another assignment
        another = input("Do you want to add another assignment? (y/n): ").strip().lower()
        if another != 'y':
            break

    # Calculate totals
    fa_total = 0
    sa_total = 0

    print("\nCalculating scores...")
    for assignment in assignments:
        weighted_score = (assignment['grade'] / 100) * assignment['weight']
        print(f"{assignment['name']}: {weighted_score:.1f} points")

        if assignment['category'] == 'FA':
            fa_total += weighted_score
        else:
            sa_total += weighted_score

    final_score = fa_total + sa_total
    gpa = (final_score / 100) * 5.0

    print(f"\nFinal Score: {final_score:.1f} points")
    print(f"GPA: {gpa:.1f}/5.0")
    print(f"Formative total: {fa_total:.1f}")
    print(f"Summative total: {sa_total:.1f}")

    # Save to CSV
    with open('grades.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Assignment', 'Category', 'Grade', 'Weight'])
        for a in assignments:
            writer.writerow([a['name'], a['category'], a['grade'], a['weight']])

    print("\nSaved to grades.csv")


if __name__ == "__main__":
    main()
