import pytest
from health_app.health import Health, save_records, load_records


#          TEST CREATING A VALID HEALTH RECORD
def test_valid_health_creation():
    h = Health(name="Anna", weight_kg=55, height_m=1.65)
    assert h.name == "Anna"
    assert h.weight_kg == 55
    assert h.height_m == 1.65


#          TEST CREATING AN INVALID HEALTH RECORD (MISSING NAME)
def test_invalid_health_creation():
    with pytest.raises(ValueError):
        Health(name="   ", weight_kg=55, height_m=1.65)


#          TEST FUNCTION CALCULATE_BMI
def test_calculate_bmi():
    h = Health(name="Bob", weight_kg=80, height_m=2.0)
    assert h.calculate_bmi() == 20.0


#          TEST FUNCTION CATEGORIZE_BMI
def test_categorize_bmi_underweight():
    h = Health(name="A", weight_kg=45, height_m=1.7)
    assert h.categorize_bmi() == "Underweight"

def test_categorize_bmi_normal():
    h = Health(name="B", weight_kg=65, height_m=1.7)
    assert h.categorize_bmi() == "Normal"

def test_categorize_bmi_overweight():
    h = Health(name="C", weight_kg=80, height_m=1.7)
    assert h.categorize_bmi() == "Overweight"

def test_categorize_bmi_obese():
    h = Health(name="D", weight_kg=100, height_m=1.7)
    assert h.categorize_bmi() == "Obese"


#          TEST FUNCTION GET_HEALTH_ADVICE
def test_get_health_advice_underweight():
    h = Health(name="A", weight_kg=45, height_m=1.7)
    assert "less than desired" in h.get_health_advice()

def test_get_health_advice_normal():
    h = Health(name="B", weight_kg=65, height_m=1.7)
    assert "normal for your height" in h.get_health_advice()

def test_get_health_advice_overweight():
    h = Health(name="C", weight_kg=80, height_m=1.7)
    assert "overweight" in h.get_health_advice()

def test_get_health_advice_obese():
    h = Health(name="D", weight_kg=100, height_m=1.7)
    assert "obese" in h.get_health_advice()


#          TEST FUNCTION GET_IDEAL_WEIGHT
def test_get_ideal_weight():
    h = Health(name="Eve", weight_kg=70, height_m=1.70)
    # Ideal weight = 22 * (height_m ** 2)
    expected_ideal = round(22 * (1.70 ** 2), 1)
    assert h.get_ideal_weight() == expected_ideal


#          TEST HELP FUNCTION TO_DICT
def test_to_dict():
    h = Health(name="Anna", weight_kg=55, height_m=1.65, category="Normal")
    d = h.to_dict()
    assert d["name"] == "Anna"
    assert d["weight_kg"] == 55
    assert d["height_m"] == 1.65
    assert d["category"] == "Normal"
    assert d["calculated_bmi"] == h.calculate_bmi()
    assert d["ideal_weight_diff"] == round(55 - h.get_ideal_weight(), 1)

#          TEST HELP FUNCTION SAVE_RECORDS AND LOAD_RECORDS
def test_save_and_load_records(tmp_path):
    records = [{"name": "Anna", "weight_kg": 55, "height_m": 1.65}]
    file = tmp_path / "test.json"
    save_records(records, filename=str(file))
    loaded = load_records(filename=str(file))
    assert loaded == records
