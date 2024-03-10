import csv
import os

def merge_csv_files(input_folder, output_file):
    # Get a list of all CSV files in the input folder
    csv_files = [file for file in os.listdir(input_folder) if file.endswith('.csv')]

    # Ensure the output file is opened in append mode to avoid overwriting existing data
    with open(output_file, 'a', newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file)

        # Iterate over each CSV file
        for csv_file in csv_files:
            csv_file_path = os.path.join(input_folder, csv_file)
            
            # Open the current CSV file for reading
            with open(csv_file_path, 'r', newline='', encoding='utf-8') as in_file:
                reader = csv.reader(in_file)
                # Skip the header in subsequent files
                if csv_files.index(csv_file) > 0:
                    next(reader)
                # Write each row from the current CSV file to the output file
                for row in reader:
                    writer.writerow(row)

if __name__ == "__main__":
    input_folder = "Data"  # Specify the path to the folder containing CSV files
    output_file = "merged_output.csv"  # Specify the name of the output file

    merge_csv_files(input_folder, output_file)
    print("CSV files merged successfully.")
