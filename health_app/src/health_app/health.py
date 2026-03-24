from pydantic import BaseModel, validator
import json
import os


class Health(BaseModel):
    name: str
    weight_kg: float
    height_m: float
    category: str = ""

    @validator('name')
    def name_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Name cannot be empty')
        return v

    def calculate_bmi(self):
            return round(self.weight_kg / (self.height_m ** 2), 2)

    def categorize_bmi(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def get_health_advice(self) -> str:
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Your weight is less than desired. To maintain a healthy body increase intake of food and water"
        elif bmi < 25:
            return "Your weight is normal for your height and weight. You don't need to implement lifestyle changes"
        elif bmi < 30:
            return "Your weight is considered overweight. Please monitor intake of food and increase your daily activity"
        else:
            return "Your weight is considered obese. This is the time to drastically decrease intake of food while starting exercising regularly"

    def get_ideal_weight(self) -> float:
            return round(22 * (self.height_m ** 2), 1)


    #          HELPER FUNCTION THAT TURN HEALTH ATTRIBUTES TO A DICTIONARY
    def to_dict(self):
        ideal_weight = self.get_ideal_weight()
        weight_diff = round(self.weight_kg - ideal_weight, 1)
        list_object = {
            "name": self.name,
            "weight_kg": self.weight_kg,
            "height_m": self.height_m,
            "category": self.category,
            "calculated_bmi": self.calculate_bmi(),
            "ideal_weight_diff": weight_diff
        }
        return list_object


#          HELP FUNCTION SAVE
def save_records(records, filename="health_records.json"):
    with open(filename, "w") as f:
        json.dump(records, f, indent=2)

#          HELP FUNCTION LOAD
def load_records(filename="health_records.json"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        data = json.load(f)
    return data


