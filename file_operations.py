# Function to update the parameter in the file passed as an argument to the value passed in the argument
def update_server_config(file_path, parameter, value):
    # try catch blocks for exception handling
    try:
        with open(file_path, "r") as file: # open and read the file
            lines = file.readlines() # Store the data inside file in a variable called lines in a form of list

        with open(file_path, "w") as file:
            for line in lines:
                if parameter in line:
                    file.write(f"{parameter}={value}\n")
                else:
                    file.write(line)

    except FileNotFoundError:
        print(f"Unable to make changes. The file {file_path} does not exist.")
    
    except PermissionError:
        print(f"Unable to open file. Permission to the file {file_path} denied!")



##### Calling the function #####
# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '1000'  # New maximum connections allowed

# Update the server configuration file
update_server_config(server_config_file, key_to_update, new_value)
