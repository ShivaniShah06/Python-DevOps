import os

def list_of_dir(folder_path):
        try:
            files = os.listdir(folder_path)
            return files, None
        except FileNotFoundError:
            #print("\n !!! Please provide a valid folder path. Folder " + folder_path + " not found!")
            return None, "Folder not found!"
        except PermissionError:
            #print("\n !!! Can't list files in " + folder_path + ". Access denied!")
            return None, "Permission denied!"

def main():
    folder_paths = input("Please provide paths of folders separated by spaces: ").split()
    for folder_path in folder_paths:
        files, error = list_of_dir(folder_path)
        if files:
            print("\n ***** List of files in folder: " + folder_path + " *****")
            for file in files:
               print(file)
        else:
            print("\n" + folder_path + ": " + error)

if __name__ == "__main__":
    main()
    


# ============= Initial code=============:
# import os

# folder_paths = input("Please provide paths of folders separated by spaces: ").split()

# for folder_path in folder_paths:
#     try:
#         files = os.listdir(folder_path)

#     except FileNotFoundError:
#         print("\n !!! Please provide a valid folder path. Folder " + folder_path + " not found!")
#         continue
#     except PermissionError:
#         print("\n !!! Can't list files in " + folder_path + ". Access denied!")
#         continue
#     print("\n ***** List of files in folder: " + folder_path + " *****")
#     for file in files:
#         print(file)