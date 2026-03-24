import pytest
from health_app.data import get_statistics
from health_app.health import save_records

#          TEST STATISTICS FUNCTION
def test_get_statistics(tmp_path):
    records = [
        {"name": "Alice", "weight_kg": 60, "height_m": 1.65, "category": "Normal", "calculated_bmi": 22.0, "ideal_weight_diff": 0.0},
        {"name": "Bob", "weight_kg": 80, "height_m": 1.80, "category": "Overweight", "calculated_bmi": 24.6, "ideal_weight_diff": 5.0},
        {"name": "Jerry", "weight_kg": 90, "height_m": 1.60, "category": "Overweight", "calculated_bmi": 23.3, "ideal_weight_diff": 33.7}
    ]
    file = tmp_path / "test.json"
    save_records(records, filename=str(file))
    stats = get_statistics(filename=str(file))

   #          IS COUNTING NUMBER OF RECORDS CORRECT?
    assert stats["total_records"] == 3
    #          TESTING AVERAGE BMI
    assert round(stats["avg_bmi"], 1) == 23.3
    #          TESTING MOST COMMON CATEGORY
    assert stats["most_common_category"] == "Overweight"
    #          TESTING DISTRIBUTION OF CATEGORIES
    assert stats["category_distribution"] == {"Normal": 1, "Overweight": 2}
