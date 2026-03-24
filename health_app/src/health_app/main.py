from myapp import Health, save_records, load_records, get_statistics


#          ADD_RECORD FUNCTION
def add_record():
    input_name = input("What is your name? ")
    input_weight = input("What is your weight? ")
    input_height = input("What is your height? ")
    try:
        health = Health(
            name=input_name,
            weight_kg=float(input_weight),
            height_m=float(input_height)
        )
        category = health.categorize_bmi()
        health.category = category
        bmi = health.calculate_bmi()
        ideal_weight = health.get_ideal_weight()
        advice = health.get_health_advice()

        print(f"Added {health.name}: BMI {bmi:.2f} ({category}) | Ideal: {ideal_weight:.1f}kg | Advice: {advice}")

        records = load_records()
        records.append(health.to_dict())
        save_records(records)
        print("Record added.")
    except Exception as e:
        print("Invalid input, please try again")

#          VIEW HEALTH RECORDS FUNCTION
def view_health_records():
    records = load_records()
    if not records:
        print("No health records found.")
    else:
        for i, record in enumerate(records, 1):
            print(f"\nRecord {i}:")
            print(f"  Name: {record['name']}")
            print(f"  Weight (kg): {record['weight_kg']}")
            print(f"  Height (m): {record['height_m']}")
            print(f"  Category: {record['category']}")
            print(f"  BMI: {record['calculated_bmi']}")
            print(f"  Ideal Weight Diff (kg): {record['ideal_weight_diff']}")

#          WATCH STATISTICS FUNCTION
def view_statistics():
    stats = get_statistics()
    print("\nStatistics:")
    print(f"Total records: {stats['total_records']}")
    print(f"Average BMI: {stats['avg_bmi']:.2f}")
    print(f"Most common category: {stats['most_common_category']}")
    print("Category distribution:")
    for category, count in stats['category_distribution'].items():
        print(f"  {category}: {count}")

#          SAVE AND QUIT FUNCTION
def save_and_quit():
    print("Saving and quitting!")
    exit()

while True:
    print("1. Add a health record")
    print("2. View all health records")
    print("3. View statistics")
    print("4. Save and quit")

    user_input = input("What do you want to do? ")

    if user_input == "1":
        add_record()
    elif user_input == "2":
        view_health_records()
    elif user_input == "3":
        view_statistics()
    elif user_input == "4":
        save_and_quit()
    else:
        print("Invalid choice. Try again.")