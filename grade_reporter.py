
# Grade Reporter

grades = [85, 72, 90, 45, 68, 55, 33, 78]

total = 0
passed = 0
failed = 0

print("===== GRADE REPORT =====")

for grade in grades:
    total += grade

    if grade >= 80:
        result = "A"
    elif grade >= 70:
        result = "B"
    elif grade >= 60:
        result = "C"
    elif grade >= 50:
        result = "D"
    else:
        result = "F"

    if grade >= 50:
        passed += 1
    else:
        failed += 1

    print(f"Grade: {grade} | Result: {result}")

average = total / len(grades)

print("\n===== SUMMARY =====")
print(f"Number of students: {len(grades)}")
print(f"Total marks: {total}")
print(f"Average mark: {average:.2f}")
print(f"Students passed: {passed}")
print(f"Students failed: {failed}")
