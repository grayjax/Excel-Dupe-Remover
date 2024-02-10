import pandas as pd
import os

def get_unique_output_path(path):
    counter = 1
    output_path = path
    file_name, file_extension = os.path.splitext(path)

    while os.path.exists(output_path):
        output_path = f"{file_name}_{counter}{file_extension}"
        counter += 1

    return output_path

input_csv_path = r'C:\Users\serap\Desktop\AL Lps.csv'
output_csv_path = r'C:\Users\serap\Desktop\AL Lps2.csv'

# Read the input .csv file
data = pd.read_csv(input_csv_path)

# Remove duplicates in each column separately
for column in data.columns:
    data[column] = data[column].drop_duplicates(keep='first').reset_index(drop=True)

# Check if the output file already exists and get a unique output path if needed
unique_output_path = get_unique_output_path(output_csv_path)

# Save the modified data to a new .csv file
data.to_csv(unique_output_path, index=False)

print(f'Saved the cleaned data to {unique_output_path}')
