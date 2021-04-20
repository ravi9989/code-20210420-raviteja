from bmi_processor.bmi_processor import caluclate_bmi

# import pty

def test_ht_175_wt_60():

    assert caluclate_bmi(175, 60) == 19.6

def test_ht_0_wt_55():

    assert caluclate_bmi(0, 55) == -1

def test_ht_175_wt_0():

    assert caluclate_bmi(175, 0) == 0