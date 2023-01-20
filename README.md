# Matching-Project

## Student-Mentor Matching Algorithm

This code implements an algorithm to match students with mentors based on their preferences and qualifications. The algorithm uses a "D-Matrix" and "finalList" to determine the best matches.

## Requirements

- Python 3.x
- csv
- math
- pprint

## Usage

1. Run the code using python3.

        python3 testfile.py

2. Two CSV files, "Questionnaire_Mentees.csv" and "Questionnaire_Mentors.csv" are read and processed to get the student and mentor preferences respectively.
3. The calcDmatrix function is called to calculate the D-Matrix.
4. The calcList function is called to calculate the finalList.
5. The best matches are returned as a list of lists

## Input format

The input CSV files should have the following format:

- The first column should be a unique identifier for the student/mentor.
- The following columns should be the student/mentor's preferences and qualifications, separated by semicolons if they have multiple options.

## Customization

- The listDict variable contains a list of dictionaries that map the strings in the input CSV file to integers. You can customize this to match your specific needs.
- The calcDvalue function is used to calculate the values in the D-Matrix. You can modify this function to change the algorithm used to determine the similarity between a student and mentor.
- The dummyDvalue variable is used to add dummy values to the D-Matrix. You can adjust this value to change the number of dummy values added.

## Output

The final matches are returned as a list of lists. Each inner list contains the index of the student and the index of their matched mentor.

## Limitations

- The code assumes that the input CSV files are well-formed and contain no errors.