import os

# Path to the folder containing your .vhd files
folder_path = "./files"

# Name of the output .txt file
output_file = "output.txt"

# Open the output file in append mode
with open(output_file, 'a') as output:
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter for .vhd files
    vhd_files = sorted([file for file in files if file.endswith(".vhd")])
    
    # Iterate through each .vhd file and append its contents to the output file
    for vhd_file in vhd_files:
        with open(os.path.join(folder_path, vhd_file), 'r') as file:
            output.write(f"Contents of {vhd_file}:\n----------------------------------------------------------------------------------\n")
            output.write(file.read())
            output.write("\n\n")

print("Files have been appended to", output_file)
