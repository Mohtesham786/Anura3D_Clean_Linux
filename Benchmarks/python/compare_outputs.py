""" Compares the outputs from Anura3D and the stashed files that are deemed correct """
import os
import numpy as np
import pandas as pd

# def load_output(filename):
#     """Load output data from a file."""
#     return np.loadtxt(filename)

# def compare_outputs(actual_file, expected_file, tolerance=1e-6):
#     """Compare actual output with expected output."""
#     actual = load_output(actual_file)
#     expected = load_output(expected_file)
    
#     if actual.shape != expected.shape:
#         return False, f"Shape mismatch: actual {actual.shape}, expected {expected.shape}"
    
#     diff = np.abs(actual - expected)
#     max_diff = np.max(diff)
    
#     if max_diff > tolerance:
#         return False, f"Max difference {max_diff} exceeds tolerance {tolerance}"
    
#     return True, "Outputs match"

def compare_files(file1_path, file2_path):
    """
    Compare the files passed in. If they don't match set passed to false and return the information that is different
    """

    # Open the files and read all of the lines
    with open(file1_path, 'r', newline=None) as f1, open(file2_path, 'r', newline=None) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    
    # Init list to track the differences between the files
    differences = []

    # Get the max number of lines in 
    max_lines = max(len(lines1), len(lines2))
    
    # print the actual file
    print(file1_path)

    for i in range(max_lines):
        # Get the line i of the file if i is not greater than the length of the file
        line1 = " ".join(lines1[i].split()) if i < len(lines1) else None
        line2 = " ".join(lines2[i].split()) if i < len(lines2) else None
        if line1 != line2:
            differences.append((i + 1, line1, line2))
    
    if len(differences) > 0:
        passed = False
        message = "The test failed. The differences are: \n" + \
                   "Line #    ---- Actual -----   ---- Expected ----- \n" + \
                   "\n".join(map(str, differences)) + "\n"
    else:
        passed = True
        message = "The test passed"

    return passed, message

def compare_file_as_dfs(file_1_path, file_2_path, tolerance = 1e-4):
    """
    Load in two files and compare them as dfs
    Assumes that the columns are all the same
    """


    # Store the first file as a df
    df1 = pd.read_csv(file_1_path, sep = "\\s+")

    # Store the second as a df
    df2 = pd.read_csv(file_2_path, sep = "\\s+")

    diff = df1 - df2

    abs_diff = np.abs(diff)
    
    # Check if the difference are with the tolerance
    within_tolerance = abs_diff <= tolerance

    # Check if all values are with the tolerance
    all_within_tolerance = within_tolerance.all().all()

    if all_within_tolerance:
        passed = True
        message = "The test passed"
    else:
        passed = False
        message = "The test failed"

    return passed, message

def run_comparisons():
    """Run comparisons for all test cases."""

    script_dir = os.path.dirname(__file__)

    # Benchmark root folder
    benchmark_folder_path = os.path.abspath(os.path.join(script_dir, ".."))

    print("Benchmark root:", benchmark_folder_path)
    print("Folders inside benchmark root:", os.listdir(benchmark_folder_path))

    # Add explicit test cases here
    test_cases = [
        # Existing wave ENG comparison
        ("wave/wave_small_001.ENG", "wave/wave_small_001_expected.ENG"),

        # Example BMR/BMS comparisons
        # Replace these expected file names with your real stored reference files
        ("Pre-Commit_Tests/4007_lineartraction/LinearLoad.A3D/LinearLoad.BMR",
         "Pre-Commit_Tests/4007_lineartraction/LinearLoad.A3D/LinearLoad_expected.BMR"),

        ("Pre-Commit_Tests/4007_lineartraction/LinearLoad.A3D/LinearLoad.BMS",
         "Pre-Commit_Tests/4007_lineartraction/LinearLoad.A3D/LinearLoad_expected.BMS"),

        ("Pre-Commit_Tests/4008_lineargravity/LinearLoad.A3D/LinearLoad.BMR",
         "Pre-Commit_Tests/4008_lineargravity/LinearLoad.A3D/LinearLoad_expected.BMR"),

        ("Pre-Commit_Tests/4008_lineargravity/LinearLoad.A3D/LinearLoad.BMS",
         "Pre-Commit_Tests/4008_lineargravity/LinearLoad.A3D/LinearLoad_expected.BMS"),
    ]

    all_passed = True

    for actual_file, expected_file in test_cases:
        actual_file = os.path.join(benchmark_folder_path, actual_file)
        expected_file = os.path.join(benchmark_folder_path, expected_file)

        # Check file existence first
        if not os.path.exists(actual_file):
            print(f"FAILED: actual file not found: {actual_file}")
            all_passed = False
            continue

        if not os.path.exists(expected_file):
            print(f"FAILED: expected file not found: {expected_file}")
            all_passed = False
            continue

        passed, message = compare_files(actual_file, expected_file)

        print(f"Comparing {actual_file} with {expected_file}:")
        print(f"  {'PASSED' if passed else 'FAILED'}: {message}")

        all_passed = all_passed and passed

    return all_passed
    
if __name__ == "__main__":
    # Run the comparisons
    all_passed = run_comparisons()
    print("made it through the check")
    exit(0 if all_passed else 1)
