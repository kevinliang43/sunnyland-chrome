# Setup/Installation
## Python Requirements
This script was built with Python3. You can install Python3 [here](https://www.python.org/downloads/).

## Dependencies
Run the following command to install the script dependencies.
`pip3 install requirements.txt`

# Usage
## Get started

There are only two requirements when running the script, `input_path` (represented by the `-i` flag) and `mass_shift` (represented by the `-m` flag).
To execute the script (with just the required arguments), simply run the following command:

```./peaks_finder_driver -i <input_path> -m <mass_shift>```

## More Details

There are other optional arguments for the script (details below):

```
usage: peaks_finder_driver [-h] -i INPUT_PATH -m MASS_SHIFT [-t INTENSITY_TOLERANCE]
                           [-v MASS_TOLERANCE] [-o OUTPUT_PATH]

Centroid Mass / Relative Intensity peaks finder tool

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_PATH, --input_path INPUT_PATH
                        Filepath of the input file.
  -m MASS_SHIFT, --mass_shift MASS_SHIFT
                        Mass Shift to look for
  -t INTENSITY_TOLERANCE, --intensity_tolerance INTENSITY_TOLERANCE
                        Accepted tolerance for intensity to match
  -v MASS_TOLERANCE, --mass_tolerance MASS_TOLERANCE
                        Accepted tolerance for Mass shift to match
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        Destination filepath of the script output file.
```

# Examples
## Script with Input File example
`./peaks_finder_driver.py -i test_files/TGase_Bromonitro_Mass_List.xlsx -m 2`

## Single File Output: 
![image](https://user-images.githubusercontent.com/15353453/75598785-738fe780-5a6c-11ea-8e11-8e3ddba0f8d1.png)


## Script with Input Directory Example
`./peaks_finder_driver.py -i test_files/ -m 2`

## Directory Example Output
![image](https://user-images.githubusercontent.com/15353453/75598806-b05bde80-5a6c-11ea-8650-76cb328bab56.png)

# Notes
- If an output filepath (denoted by the `-o` flag) is not specified, default directory for script outputs will be created (if it doesn't exist already) in `sunnyland-chrome/output/` and a filepath will be generated in the form of: `sunnyland-chrome/output/peaks_<current_time>.xlsx`, with `current_time` in the form of `%Y_%m_%d-%H%M%S`
- Required arguments will be the `input_path`(`-i` flag) and `mass_shift` (`-m` flag).
- Optional arguments will be `intensity_tolerance` (`-t` flag, default=0.1), `mass_tolerance` (`-v` flag, default=0.001), and `output_path` (`-o` flag)
- Due to a depreciation of one of the dependencies of pandas in read_excel, we cannot read `.xls` files. As of now this script ONLY takes in `.xlsx` files. Link to the relevant issue is documented here: https://github.com/pandas-dev/pandas/issues/11503
