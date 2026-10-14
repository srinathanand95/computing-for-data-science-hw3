# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    if light == 'green':
        return 'go'
    elif light == 'yellow':
        return 'wait'
    elif light == 'red':
        return 'stop'
    else:
        raise ValueError(f'Undefined instruction for color: {light}')

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

def safe_subtract(x, y):
    try:
        return x - y
    except TypeError:
        return None
    except Exception as e:
        print(f'Subtraction failed: {e}')
    

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that return the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl


def retrieve_age_eafp(dic):
    try:
        return 2026 - dic['birth']
    except KeyError:
        print('This dictionary does not have birth data!')
        
    
def retrieve_age_lbyl(dic):
    if 'birth' in dic:
        return 2026 - dic['birth']
    else:
        print('This dictionary does not have birth data!')
# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that takes the path to the file as an argument
# and reads the file making sure to use to handle the fact
# that it might not exist. 

def read_data(path):
    try:
        with open(path, 'r') as file:   # can also use pandas to read .csv files.
            data = file.read()
            return data
    except FileNotFoundError:
        return f'File not found: {path}. Make sure the file exists and you are providing the correct path.'

# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them

### (a)
# total_double_sum = 0           # original code
# for elem in [10, 5, 2]:
    # double = elem * 2
    # total_double_sum += elem

# Logical error: The original code was adding the original element (elem) to total_double_sum instead of the 
# doubled value (double). The corrected line is now adding double to total_double_sum.

total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double  # Adds elem*2 to total_double_sum, totalling 34

#=======================================================================
### (b)
# strings = ''                    # original code
# for string in ['I', 'am', 'Groot']:
    # strings = string+"_"+string

# Logical error: We are overwriting the variable 'strings' in each iteration of the loop, so at the end of the loop, 
# 'strings' will only contain the last value. If we want to concatenate all the strings, we should use '+=' 
# instead of '='.

# Logical error: We are concatenating the string with itself, which may not be the intended behavior. If we want to 
# concatenate the strings with an underscore, we should use 'strings += string + "_"' instead.

strings = ''
for string in ['I', 'am', 'Groot']:
    strings += string + "_"       # writes "I_am_Groot_"

#=======================================================================
### (c)                           # orginal code
# j=10
# while j > 0:
#    j += 1

# Logical error: We are creating an infinite loop, because j is always increasing and will never be <= 0.
# If we wish to create a countdown loop, we should decrement j instead of incrementing it.

j = 10
while j > 0:
    # print(j)                    # not necessary, but it will print the countdown in case we wanted to see it
    j -= 1                        # stops the countdown when j is 0

#=======================================================================
### (d)
# productory = 0                  # original code
# for elem in [1, 5, 25]:
    # productory *= elem

# Logical error: The variable 'productory' is initialized to 0, which will always result in a 0 regardless of the 
# elements in the list for the product. If we can initialize 'productory' to 1 instead of 0 to get the correct product.

productory = 1
for elem in [1, 5, 25]:
    productory *= elem           # multiplies each element in the list to get the product, resulting in 125