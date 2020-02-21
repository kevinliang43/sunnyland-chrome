import numpy as np
import pandas as pd
import re


def clean_table(table_df):
    """
    1. Cleans a DataFrame by removing all NaN rows and columns, extracting just the table needed.
    2. If DataFrame headers are unnamed, Headers will be set to elements in the first row after cleaning.
    :param table_df: DataFrame representing a single excel sheet
    :return: DataFrame
    """
    # Remove all NaN rows and columns
    table_df.dropna(axis='columns', how='all', inplace=True)
    table_df.dropna(axis='rows', how='all', inplace=True)

    # If headers are unnamed, set first row as headers
    table_df.columns = table_df.iloc[0]  # Set headers to the first row containing the headers
    table_df.drop(table_df.index[0], inplace=True)  # Remove the first row
    return table_df


def find_peaks(table_df, intensity_tolerance, mass_shift, mass_shift_tolerance):
    """
    Find the peaks for a given set of Centroid Mass/ Relative Intensity data points

    :param table_df: (DataFrame) DataFrame containing Centroid Mass in column 0 and Relative Intensity in column 1
    :param intensity_tolerance: (float) Accepted tolerance for the difference in intensities
    :param mass_shift: (int) Mass Shift
    :param mass_shift_tolerance: (float) Accepted tolerance for the difference in Mass Shift
    :return: list of peak tuples in the form of [[mass_1, intensity_1, mass_2, intensity_2], ...]
    """

    table_arr = table_df.values
    peaks = []  # Initialize a list of of peaks tuples
    mass_shift_upper = mass_shift + mass_shift_tolerance  # Upper bound for mass_shift with tolerance
    mass_shift_lower = mass_shift - mass_shift_tolerance  # Lower bound for mass_shift with tolerance

    for row_idx in range(len(table_arr)):
        # Current row variables
        current_row = table_arr[row_idx]
        current_row_mass = current_row[0]
        current_row_intensity = current_row[1]

        # Initialize compare_row index to 1 greater than current row
        compare_row_idx = row_idx + 1

        # Loop until we find row with correct mass_shift added to the current row
        while compare_row_idx < len(table_arr):
            compare_row = table_arr[compare_row_idx]
            compare_row_mass = compare_row[0]
            compare_row_intensity = compare_row[1]

            # Continue to the next row if mass shift is exceeded
            if abs(current_row_mass - compare_row_mass) > mass_shift_upper:
                break

            # Found the row with the correct mass shift added to current row
            elif mass_shift_upper >= abs(current_row_mass - compare_row_mass) >= mass_shift_lower and \
                    abs(current_row_intensity - compare_row_intensity) <= intensity_tolerance:
                # Append current_row and compare_row data the peaks list if intensity is a match
                peaks.append([current_row_mass, current_row_intensity, compare_row_mass, compare_row_intensity])
                break

            # Else, continue to the next row
            else:
                compare_row_idx += 1

    return peaks


def save_peaks_as_excel(peaks, file_path):
    """
    Formats a list of peak tuples into an Excel format and writes to a given filepath

    :param peaks: list of peak tuples of the form [[mass_1, intensity_1, mass_2, intensity_2], ...]
    :param file_path: file path to save Excel output to
    :return: None
    """
    columns = ['Centroid Mass 1', 'Relative Intensity 1', 'Centroid Mass 2', 'Relative Intensity Mass 2']
    df = pd.DataFrame(peaks, columns=columns)
    df.to_excel(file_path)