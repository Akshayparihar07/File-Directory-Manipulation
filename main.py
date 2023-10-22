import os
import shutil

# Function to create a directory
def create_directory():
    try:
        directory_path = input('Enter the path where you want to create a new directory: ')
        directory_name = input("Enter the name of the directory to create: ")
        
        if not directory_name or not directory_path:
            print("Directory name and path cannot be empty.")
            return
        
        path = os.path.join(directory_path, directory_name)
        
        if os.path.exists(path):
            print(f"Directory '{directory_name}' already exists.")
            return 

        os.makedirs(path)  # Use os.makedirs to create parent directories if they don't exist
        print(f"Directory '{directory_name}' has been successfully created.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to create a directory.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to delete a directory
def delete_directory():
    try:
        directory_path = input("Enter the path of the directory to delete: ")
        directory_name = input("Enter the name of the directory to delete: ")
        
        if not directory_name:
            print("Directory name cannot be empty.")
            return

        path = os.path.join(directory_path, directory_name)
        
        if not os.path.exists(path):
            print(f"Directory '{directory_name}' does not exist.")
            return

        if not os.path.isdir(path):
            print(f"'{directory_name}' is not a directory.")
            return

        try:
            shutil.rmtree(path)
            print(f"Directory '{directory_name}' has been deleted successfully.")
        except OSError as e:
            print(f"An Error occurred: {e}")

    except PermissionError:
        print(f"Permission Denied: You may not have the necessary permission to delete the directory.")
    except FileNotFoundError:
        print(f"Directory '{directory_name}' not found.")
    except NotADirectoryError:
        print(f"'{directory_name}' is not a directory.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to list files in a directory
def list_files_in_directory():
    try:
        directory_path = input("Enter the path of the directory to list files from: ")
        directory_name = input("Enter the name of the directory: ")
        
        path = os.path.join(directory_path, directory_name)

        if not os.path.exists(path):
            print(f"Directory '{directory_name}' does not exist.")
            return

        if not os.path.isdir(path):
            print(f"'{directory_name}' is not a directory.")
            return

        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

        if not files:
            print(f"No files found in '{directory_name}'.")
            return

        print(f"Files in '{directory_name}':")
        for file in files:
            print(file)  # Removed splitting into name and type for simplicity

    except PermissionError:
        print(f"Permission Denied: You may not have the necessary permission to list files in '{directory_path}'.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to rename a directory
def rename_directory():
    try:
        directory_path = input("Enter parent path of the Directory: ")
        old_directory_name = input("Enter name of the directory you want to rename: ")
        new_directory_name = input(f"Enter the name you want to rename '{old_directory_name}' to: ")

        if not old_directory_name or not directory_path or not new_directory_name:
            print("Directory names and path cannot be empty.")
            return

        old_directory_path = os.path.join(directory_path, old_directory_name)
        new_directory_path = os.path.join(directory_path, new_directory_name)

        if not os.path.exists(old_directory_path):
            print(f"Directory '{old_directory_name}' does not exist.")
            return

        if os.path.exists(new_directory_path):
            print(f"'{new_directory_name}' Already exists.")
            return

        os.rename(old_directory_path, new_directory_path)
        print(f"Directory '{old_directory_path}' has been renamed to '{new_directory_path}'.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to rename the directory.")
    except FileNotFoundError:
        print(f"Directory '{old_directory_path}' not found.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to move all files from one directory to another
def move_all_files_from_one_directory_to_another():
    try:
        source_dir_path = input("Enter parent path of source directory: ")
        destination_dir_path = input("Enter parent path of destination directory: ")
        source_dir_name = input("Enter name of source directory: ")
        destination_dir_name = input("Enter name of the destination directory: ")

        if not source_dir_name or not destination_dir_name or not source_dir_path or not destination_dir_path:
            print("Directory names and paths cannot be empty.")
            return 

        source_dir = os.path.join(source_dir_path, source_dir_name)
        destination_dir = os.path.join(destination_dir_path, destination_dir_name)

        if not os.path.exists(source_dir) or not os.path.exists(destination_dir):
            print('Source or Destination directory does not exist.')
            return

        if not os.path.isdir(source_dir) or not os.path.isdir(destination_dir):
            print("Source or Destination path is not a directory.")
            return

        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            destination_path = os.path.join(destination_dir, filename)

            if os.path.isfile(source_path):
                shutil.move(source_path, destination_path)
                print(f"Moved file: '{source_path}' to '{destination_path}'")

        print("All files have been moved.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to move files.")
    except FileNotFoundError:
        print("File or directory not found.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to create a file
def create_file():
    try:
        file_path = input("Enter path where you want to create a file: ")
        file_name = input("Enter the name of your file: ")

        if not file_path or not file_name:
            print("File path and file name cannot be empty.")
            return

        full_file_path = os.path.join(file_path, file_name)

        if os.path.exists(full_file_path):
            print(f"File '{file_name}' already exists in the selected path.")
            return

        with open(full_file_path, "w") as file:
            pass  # Just create an empty file

        print(f"File '{file_name}' has been successfully created at '{file_path}'.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to create a file.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to delete a file
def delete_file():
    try:
        file_path = input("Enter the path to the file you want to delete: ")
        file_name = input("Enter the name of the file you want to delete (including the extension): ")

        if not file_name or not file_path:
            print("File name or path cannot be empty.")
            return

        full_file_path = os.path.join(file_path, file_name)

        if os.path.exists(full_file_path):
            os.remove(full_file_path)
            print(f"File '{file_name}' has been successfully deleted from '{file_path}'.")
        else:
            print(f"File '{file_name}' does not exist in the selected path.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to delete the file.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to edit a text file
def edit_text_file():
    try:
        file_path = input("Enter the path to the text file you want to edit: ")
        file_name = input("Enter the name of the text file you want to edit (including the extension): ")

        if not file_name or not file_path:
            print("File name or path cannot be empty.")
            return

        full_file_path = os.path.join(file_path, file_name)

        if os.path.exists(full_file_path):
            with open(full_file_path, "r") as file:
                content = file.read()
                print("Current content:")
                print(content)

            new_content = input("Enter the new content: ")

            with open(full_file_path, "w") as file:
                file.write(new_content)

            print(f"File '{file_name}' has been updated.")
        else:
            print(f"File '{file_name}' does not exist in the selected path.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to edit the file.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to copy content from one text file to another
def copy_text_file():
    try:
        source_path = input("Enter the path to the source text file: ")
        source_name = input("Enter the name of the source text file (including the extension): ")

        if not source_name or not source_path:
            print("Source file name or path cannot be empty.")
            return

        full_source_path = os.path.join(source_path, source_name)

        if not os.path.exists(full_source_path):
            print(f"Source file '{source_name}' does not exist in the selected path.")
            return

        destination_path = input("Enter the path to the destination text file: ")
        destination_name = input("Enter the name of the destination text file (including the extension): ")

        if not destination_name or not destination_path:
            print("Destination file name or path cannot be empty.")
            return

        full_destination_path = os.path.join(destination_path, destination_name)

        if os.path.exists(full_destination_path):
            print(f"Destination file '{destination_name}' already exists in the selected path.")
            return

        with open(full_source_path, "r") as source_file:
            source_file_content = source_file.read()

        with open(full_destination_path, "w") as destination_file:
            destination_file.write(source_file_content)

        print(f"Content from '{source_name}' has been successfully copied to '{destination_name}'.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to copy the files.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to list directories in a path
def list_directories():
    try:
        path = input("Enter the path to list directories from: ")

        if os.path.exists(path):
            items = os.listdir(path)
            directories = [item for item in items if os.path.isdir(os.path.join(path, item))]

            if not directories:
                print(f"No directories found in '{path}'.")
            else:
                print(f"Directories in '{path}':")
                for directory in directories:
                    print(directory)
        else:
            print(f"The specified path '{path}' does not exist.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to list directories.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to rename a file
def rename_file():
    try:
        file_path = input("Enter the path to the file you want to rename: ")
        old_file_name = input("Enter the current name of the file you want to rename (including the extension): ")
        new_file_name = input("Enter the new name for the file (including the extension): ")

        if not old_file_name or not file_path or not new_file_name:
            print("File names and path cannot be empty.")
            return

        old_file_path = os.path.join(file_path, old_file_name)
        new_file_path = os.path.join(file_path, new_file_name)

        if not os.path.exists(old_file_path):
            print(f"File '{old_file_name}' does not exist.")
            return

        if os.path.exists(new_file_path):
            print(f"'{new_file_name}' already exists.")
            return

        os.rename(old_file_path, new_file_path)
        print(f"File '{old_file_path}' has been renamed to '{new_file_path}'.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to rename the file.")
    except FileNotFoundError:
        print(f"File '{old_file_path}' not found.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Function to move a file from one directory to another
def move_file():
    try:
        source_dir_path = input("Enter the source directory path: ")
        destination_dir_path = input("Enter the destination directory path: ")
        file_name = input("Enter the name of the file to move (including the extension): ")

        if not source_dir_path or not destination_dir_path or not file_name:
            print("Directory paths and file name cannot be empty.")
            return 

        source_file_path = os.path.join(source_dir_path, file_name)
        destination_file_path = os.path.join(destination_dir_path, file_name)

        if not os.path.exists(source_file_path):
            print(f"File '{file_name}' does not exist in the source directory.")
            return

        if not os.path.exists(destination_dir_path):
            print("Destination directory does not exist.")
            return

        if not os.path.isdir(destination_dir_path):
            print("Destination path is not a directory.")
            return

        shutil.move(source_file_path, destination_file_path)
        print(f"File '{file_name}' has been moved to '{destination_file_path}'.")

    except PermissionError:
        print("Permission Denied: You may not have the necessary permission to move the file.")
    except FileNotFoundError:
        print("File or directory not found.")
    except OSError as e:
        print(f"An error occurred: {e}")

# Main menu function
def main():
    while True:
        print("\nMenu:")
        print("1. Create a Directory")
        print("2. Delete a Directory")
        print("3. List Files in a Directory")
        print("4. Rename a Directory")
        print("5. Move Files from One Directory to Another")
        print("6. Create a File")
        print("7. Delete a File")
        print("8. Edit a Text File")
        print("9. Copy Content from One Text File to Another")
        print("10. List Directories")
        print("11. Rename a File")
        print("12. Move a File")
        print("13. Quit")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            create_directory()
        elif choice == '2':
            delete_directory()
        elif choice == '3':
            list_files_in_directory()
        elif choice == '4':
            rename_directory()
        elif choice == '5':
            move_all_files_from_one_directory_to_another()
        elif choice == '6':
            create_file()
        elif choice == '7':
            delete_file()
        elif choice == '8':
            edit_text_file()
        elif choice == '9':
            copy_text_file()
        elif choice == '10':
            list_directories()
        elif choice == '11':
            rename_file()
        elif choice == '12':
            move_file()
        elif choice == '13':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
