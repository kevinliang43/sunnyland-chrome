import sys
import pandas as pd
from peaks_utils import clean_table, find_peaks, save_peaks_as_excel
from utils import parse_inputs, create_default_output_path


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

    # Read File
    table_df = pd.read_excel(input_fp)

    # Clean and parse data
    clean_table_df = clean_table(table_df)
    columns = ['Centroid Mass', 'Relative Intensity']
    mass_intensity_df = clean_table_df[columns]

    # Discover peaks
    result = find_peaks(mass_intensity_df, intensity_tolerance, mass_shift, mass_tolerance)

    # Write to output
    save_peaks_as_excel(result, output_fp)


if __name__ == "__main__":
    main()

