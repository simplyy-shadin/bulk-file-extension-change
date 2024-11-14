import os

def change_file_extensions(directory, old_extension, new_extension):
    """
    Changes the file extensions of all files in the specified directory.

    :param directory: Directory where the files are located
    :param old_extension: The current file extension to look for (e.g., '.txt')
    :param new_extension: The new file extension to change to (e.g., '.docx')
    """
    # List all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file has the old extension
        if filename.endswith(old_extension):
            # Build the full file path
            old_file_path = os.path.join(directory, filename)
            
            # Create the new file name by replacing the old extension with the new one
            new_filename = filename.replace(old_extension, new_extension)
            new_file_path = os.path.join(directory, new_filename)

            # Rename the file (change its extension)
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    # Get user inputs for the directory, old extension, and new extension
    directory = input("Enter the directory path where the files are located: ")
    old_extension = input("Enter the old extension to change (e.g., '.txt'): ")
    new_extension = input("Enter the new extension to change to (e.g., '.docx'): ")

    # Call the function to change the file extensions
    change_file_extensions(directory, old_extension, new_extension)
