# local and global variables

global_variable = "Global Value"

def my_function():
    local_variable = "Local Value"
    print("Inside function - Local Variable:", local_variable)
    print("Inside function - Global Variable:", global_variable)

my_function()
print("Outside function - Global Variable:", global_variable)

# You can also modify a global variable inside a function using the 'global' keyword:

def modify_global():
    global global_variable
    global_variable = "Modified Global Value"

modify_global()
print("Outside function - Modified Global Variable:", global_variable)