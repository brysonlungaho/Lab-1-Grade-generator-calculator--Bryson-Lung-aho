# Lab-1-Grade-generator-calculator--Bryson-Lung-aho
Grade Generator & CSV Organizer
Overview

This project contains two scripts to manage student grades:

Python Grade Generator (grade-generator.py)

Collects multiple assignment details interactively.

Validates input for category, grade, and weight.

Calculates weighted scores, final grade, and GPA.

Exports all data to grades.csv.

Automatically archives any existing grades.csv into an archive/ folder with a timestamp before creating a new file.

Shell CSV Organizer (organizer.sh)

Archives all CSV files in the current directory into archive/.

Adds a timestamp to the filename to avoid overwriting.

Logs all operations to organizer.log.

Requirements

Python 3.x

Bash (Linux/macOS/WSL) for the shell script

Usage
Python Grade Generator

Run the script:

python3 grade-generator.py


Follow the prompts to enter assignment names, categories (FA/SA), grades (0–100), and weights (positive numbers).

Press Enter for assignment name to finish input.

The script will calculate scores, display totals and GPA, and save grades.csv.

If a previous grades.csv exists, it will be automatically archived in archive/.

Shell CSV Organizer

Make the script executable:

chmod +x organizer.sh


Run the script in the folder containing CSV files:

./organizer.sh


All CSV files will be moved to archive/ with a timestamp, and the process is logged in organizer.log.

Notes

The Python script automatically handles archiving for grades.csv.

The shell script can archive any CSV file in the current directory.

Keep the archive/ folder tidy, as old CSVs accumulate over time.
