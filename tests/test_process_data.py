from bmi_processor.bmi_processor import process_data

case_1 = [{"Gender" : "Male", "HeightCm" : 161, "WeightKg" : 85}]
    
case_2 = [{"Gender" : "Female", "HeightCm" : 163, "WeightKg" : 87}]

case_3 = [{"Gender" : "Male", "HeightCm" : 168, "WeightKg" : 71}]

out_1 = [{
        "Gender": "Male",
        "HeightCm": 161,
        "WeightKg": 85,
        "bmi_category": "moderate obese",
        "health_risk": "medium risk",
        "bmi": 32.8
    }]
out_2 = [{
        "Gender": "Female",
        "HeightCm": 163,
        "WeightKg": 87,
        "bmi_category": "moderate obese",
        "health_risk": "medium risk",
        "bmi": 32.7
    }]
out_3 = [{
        "Gender": "Male",
        "HeightCm": 168,
        "WeightKg": 71,
        "bmi_category": "over weight",
        "health_risk": "enhanced risk",
        "bmi": 25.2
    }]

def test_1():

    assert process_data(case_1) == out_1

def test_2():

    assert process_data(case_2) == out_2

def test_3():

    assert process_data(case_3) == out_3
    