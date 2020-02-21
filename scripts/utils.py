import argparse
import os
import time


def parse_inputs(argv):
    """
    Parses command Line arguments and returns them in a dictionary format
    :param argv: list of command line arguments to be parsed
    :return: dictionary of args
    """
    parser = argparse.ArgumentParser(description='Centroid Mass / Relative Intensity peaks finder tool')
    parser.add_argument("-i", "--input_path", help="Filepath of the input file.", required=True, type=str)
    parser.add_argument("-m", "--mass_shift", help="Mass Shift to look for", required=True, type=float)

    parser.add_argument("-t", "--intensity_tolerance", help="Accepted tolerance for intensity to match",
                        required=False, default=0.01, type=float)
    parser.add_argument("-v", "--mass_tolerance", help="Accepted tolerance for Mass shift to match",
                        required=False, default=0.001, type=float)
    parser.add_argument("-o", "--output_path", help="Destination filepath of the script output file.", required=False)
    args = parser.parse_args()
    return vars(args)


def create_default_output_path():
    """
    Creates a default output directory and returns a default output file path.
    :return: (str) output file path
    """

    # Create target output directory within the parent directory
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = "{}/output".format(parent_dir)

    # Create the default output directory if it doesn't already exist
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    # Return the default output file path string
    current_time = time.strftime("%Y_%m_%d-%H%M%S")
    return "{}/peaks_{}.xlsx".format(output_dir, current_time)
