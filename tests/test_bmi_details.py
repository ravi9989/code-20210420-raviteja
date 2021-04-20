from bmi_processor.bmi_processor import get_bmi_details

def test_bmi_23():

    assert get_bmi_details(23) == {
        "bmi_category": "normal weight",
        "health_risk": "low risk",
        "bmi": 23
    }

def test_bmi_32_8():

    assert get_bmi_details(32.8) == {
        "bmi_category": "moderate obese",
        "health_risk": "medium risk",
        "bmi": 32.8
    }

def test_bmi_0():

    assert get_bmi_details(-1) == {
        "bmi_category": "NA",
        "health_risk": "NA",
        "bmi": -1
    }

