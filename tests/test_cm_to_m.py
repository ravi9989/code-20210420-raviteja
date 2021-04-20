from bmi_processor.bmi_processor import convert_cm_to_m

import pytest 


def test_165():

    assert convert_cm_to_m(165) == 1.65

def test_175():

    assert convert_cm_to_m(175) == 1.75

def test_0():

    assert convert_cm_to_m(0) == 0