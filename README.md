# BMI - Processor


[![made-with-python](https://img.shields.io/badge/v1.0.2%20-bmi_processor-1f425f.svg)](https://pypi.org/project/bmi-processor-beta/)

BMI processor is a package that processes the json data with heights and weights and categorize the health risk and bmi category

## Tech

Python 

- binary-search using bisect library to get the range where bmi falls in
- json library used for rreading and writing json input/ouput files
- pytest for testing each function in the package to ensure correct CI
- Used github actions for CD to publish the package in PYPI on every release 


## Installation

This package is built using default python libraries
```
pip3 install bmi-processor-beta
```

## Usage 
 - take json file of hights and weights sample data
 - give input_file_name and ouput_file_name
 
 Example:
   ```python3
   status, message = process_bmi_json_files('../data/test.json', '../data/test_out.json')   
   ```
## TODO

- [ ] to automate the creation of release on tag creation
- [ ] plotting analytics for the processed json data

## License

MIT

