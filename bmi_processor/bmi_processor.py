import bisect
import os
import json
from functools import lru_cache

"""
made the ranges as a sorted list and when we want to decide in which Range BMI will falls
simply binary search for the place where we can insert our caluclated BMI without distrubing sorted order
if the index is even then it belogs (even_index, even_index+1)
else index will be reduced by one follow the same as even condition
"""
Ranges = [0,18.4, 18.5, 24.9, 25, 29.9, 30, 34.4, 35, 39.9, 40, 101]

"""
categorised as index as if BMI falls in 1st range then the catgory and health risk falls in 1st index

"""
Categories = {
    -1 : {'bmi_category' : 'NA', "health_risk" : 'NA', "bmi" : -1},
    1 : {'bmi_category' : 'under weight', "health_risk" : 'malnutrion risk', "bmi" : 0},
    2 : {'bmi_category' : 'normal weight', "health_risk" : 'low risk', "bmi" : 0},
    3 : {"bmi_category" : 'over weight', "health_risk" : 'enhanced risk',"bmi" : 0},
    4 : {"bmi_category" : 'moderate obese', "health_risk" : 'medium risk', "bmi" : 0},
    5 : {"bmi_category" : 'severly obese', "health_risk" : 'high risk', "bmi" : 0},
    6 : {"bmi_category" : 'very severe obese', "health_risk" : 'very very high risk', "bmi" : 0}
}


@lru_cache(maxsize=128)
def get_bmi_details(bmi):

    """
    input : int
    output : dict
    binary searched for position where i can insert the BMI so that the sort property wont loose
    and returning the category details
    """

    if bmi == -1:
        
        return Categories[-1]

    idx = bisect.bisect_right(Ranges,bmi)-1
    if idx%2 != 0:
        idx -= 1
    
    Categories[idx/2 + 1]["bmi"] = bmi

    return Categories[idx/2 + 1]



def convert_cm_to_m(cm):
    """
    cm --> m
    """
    return cm / 100.0


def caluclate_bmi(hight, weight):

    """
    BMI = weight/ (hight^2) 

    """
    try:

        hight = convert_cm_to_m(hight)
        return round(weight/(hight**2), 1)

    except:

        return -1


"""
when there is large file like lacs we can make one json file to multiple chunk sized files and 
processing them saperatly

with open('file.json') as infile:
  whole_file = json.load(infile)
  chunk_size = 10000
  for i in range(0, len(whole_file), chunk_size):
    with open('bmi_data_' + str(i//chunk_size) + '.json', 'w') as outfile:
      json.dump(o[i:i+chunk_size], outfile)

"""


def read_json(file_name):
    """
    read json file
    """
    try: 

        with open(file_name) as f:
            data = json.load(f)
        
        return data

    except Exception:

        raise Exception


def write_json(file_name, json_data):
    try:

        json_object = json.dumps(json_data, indent = 4)
        with open(file_name, "w") as outfile:
            outfile.write(json_object)

        return True
        
    except:

        raise Exception


def process_data(data):

    """
    iterating and processing each record by using above helper functions
    """

    if not data:

        return {}

    record = 0
    for i in data:

        if i.get("HeightCm", "") and i.get("WeightKg", ""):

            print("processing ---- record ----", record, "--->", i)

            bmi = caluclate_bmi(i["HeightCm"], i["WeightKg"])

            bmi_category_details = get_bmi_details(bmi)

            i.update(bmi_category_details)
        
        else:

            print("failed to process ---- record ----", record, "--->", i)

        record += 1

    return data

def process_bmi_json_files(input_file, ouptut_file):

    try: 

        json_data = read_json(input_file)

        processed_data = process_data(json_data)

        if not process_data:

            return False, "exit_code 1 no data to process"
        
        write_status = write_json(ouptut_file, processed_data)

        if not write_status:
            print("exit code 1")

            return False, "exit_code 1 problem while writing into ouput file"

        return True, "Completed"

    except:

        return False, Exception 


# status, message = process_bmi_json_files('../data/test.json', '../data/test_out.json')
# print(status, message)
