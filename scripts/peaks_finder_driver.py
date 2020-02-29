import sys
import os
import pandas as pd
from peaks_utils import clean_table, find_peaks, save_peaks_as_excel
from utils import parse_inputs, create_default_output_path, list_directory_files

SHEET_NAME = 'Peaks Results'
INPUT_COLUMNS = ['Centroid Mass', 'Relative Intensity']  # Columns of Interest in input files
OUTPUT_COLUMNS = ['Centroid Mass 1', 'Relative Intensity 1', 'Centroid Mass 2', 'Relative Intensity Mass 2']


def main():

    # Parse arguments
    args = parse_inputs(sys.argv[1:])
    input_fp = args['input_path']
    output_fp = args['output_path']
    intensity_tolerance = args['intensity_tolerance']
    mass_shift = args['mass_shift']
    mass_tolerance = args['mass_tolerance']

    # If an output file path is not specified, create a default one.
    if not output_fp:
        output_fp = create_default_output_path()

    # Mapping of file_name to file_path
    files_mapping = {}

    # If input path is a file
    if os.path.isfile(input_fp):
        files_mapping = {os.path.split(input_fp)[1]: input_fp}

    # If input path is a directory
    elif os.path.isdir(input_fp):
        files_mapping = list_directory_files(input_fp)

    # Initialize Excel Writer
    output_writer = pd.ExcelWriter(output_fp, engine='xlsxwriter')
    workbook = output_writer.book
    worksheet = workbook.add_worksheet(SHEET_NAME)
    output_writer.sheets[SHEET_NAME] = worksheet

    # Initialize Pointer to the current row that is up next to write in
    current_row = 0

    # Iterate through all files and write to single excel file
    for file_name, file_path in files_mapping.items():

        # Read File
        table_df = pd.read_excel(file_path)

        # Clean and parse data
        clean_table_df = clean_table(table_df)
        mass_intensity_df = clean_table_df[INPUT_COLUMNS]

        # Discover peaks
        result = find_peaks(mass_intensity_df, intensity_tolerance, mass_shift, mass_tolerance)

        # Write File Name as the header for the current data section.
        worksheet.write_string(current_row, 0, file_name)
        current_row += 1  # Increment row pointer

        # Write Peaks Data
        df = pd.DataFrame(result, columns=OUTPUT_COLUMNS)
        df.to_excel(output_writer, sheet_name=SHEET_NAME, startrow=current_row, startcol=0)

        # Increment current_row pointer
        current_row += df.shape[0] + 2  # Number of rows of data written plus 2 rows for buffer

    # Close Output writer
    output_writer.close()


if __name__ == "__main__":
    main()

