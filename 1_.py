import glob
import os

# Find all txt files starting with "0_" in the current directory
files = glob.glob("0_1_/*.txt")

# Sort them (so 0_1.txt comes before 0_10.txt, etc.)
files.sort()

# Name of the output file
output_file = "1_/1_.txt"

# Open the output file in write mode (this will overwrite if it exists)
with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in files:
        print(f"Adding: {filename}")
        with open(filename, "r", encoding="utf-8") as infile:
            # Copy content with a separator (optional)
            outfile.write(infile.read())

print(f"\nDone! All files combined into {output_file}")