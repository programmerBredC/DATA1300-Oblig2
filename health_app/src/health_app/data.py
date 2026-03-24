from health_app.health import load_records

#          GET STATISTICS FUNCTION
def get_statistics(filename="health_records.json"):
    records = load_records(filename)
    #          IF NO RECORDS
    if not records:
        return {
            "total_records": 0,
            "avg_bmi": 0,
            "most_common_category": None,
            "category_distribution": {}
        }

    #          EMPTY LIST INITIALISATION
    bmi_list = []
    category_counts = {}

    #          LOOP THROUGH RECORDS TO GET BMI AND CATEGORY
    for record in records:
        bmi = record["calculated_bmi"]
        category = record["category"]
        bmi_list.append(bmi)
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    #          (RETURN) TOTAL RECORDS
    total_records = len(records)

    #          (RETURN) AVERAGE BMI
    avg_bmi = round(sum(bmi_list) / total_records, 2)

    #          (RETURN) MOST COMMON CATEGORY
    most_common_category = max(category_counts, key=category_counts.get)

    return {
        "total_records": total_records,
        "avg_bmi": avg_bmi,
        "most_common_category": most_common_category,
        "category_distribution": category_counts
    }




