#!/bin/bash

# Simple CSV Organizer

# Create archive folder if needed
mkdir -p archive

# Create or clear log file
echo "### Running Organizer: $(date) ###" > organizer.log

# Process each CSV file
for file in *.csv; do
    if [ -f "$file" ]; then
        # Create timestamped filename
        timestamp=$(date +"%Y%m%d-%H%M%S")
        new_name="archive/${file%.*}-$timestamp.csv"

        # Log and move file
        echo "Moved: $file -> $new_name" >> organizer.log
        mv "$file" "$new_name"

        echo "Archived: $file"
    fi
done

echo "COMPLETE! Kindly see organizer.log. Thank you."
