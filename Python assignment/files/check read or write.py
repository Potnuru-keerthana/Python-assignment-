import os

def check_permissions(file_path):
    read_access = os.access(file_path, os.R_OK)
    write_access = os.access(file_path, os.W_OK)
    
    if read_access:
        print(f"File {file_path} has read access.")
    else:
        print(f"File {file_path} does not have read access.")
        
    if write_access:
        print(f"File {file_path} has write access.")
    else:
        print(f"File {file_path} does not have write access.")

# Example usage:
check_permissions("example.txt")
