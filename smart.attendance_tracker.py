print("WELCOME TO THE SMART ATTENDANCE TRACKER")

total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes you attended: "))
target = 75.0

current_pct = (attended_classes / total_classes) * 100
print(f"\nYour current attendance is: {current_pct:.2f}%")

if current_pct >= target:
    print("Great job! You are safe from the default list.")
    allowed_to_skip = 0
    temp_total = total_classes
    temp_attended = attended_classes
    while True:
        temp_total += 1
        if (temp_attended / temp_total) * 100 >= target:
            allowed_to_skip += 1
        else:
            break
    print(f"You can safely skip the next {allowed_to_skip} class.")

else:
    print("Warning: Your attendance is below 75%!")
    needed_classes = 0
    temp_total = total_classes
    temp_attended = attended_classes
    while (temp_attended / temp_total) * 100 < target:
        temp_total += 1
        temp_attended += 1
        needed_classes += 1
    print(f"You need to attend the next {needed_classes} classes to hit 75%.")

