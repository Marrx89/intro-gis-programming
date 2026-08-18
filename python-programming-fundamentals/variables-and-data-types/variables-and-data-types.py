# INTRO VARIABLES AND DATA TYPES
# A. This is a sample Python script that defines a variable `num_points` and assigns it the value of 120. It then prints the value of `num_points` to the console.
num_points = 120
print(num_points)

#  B. Variable Assignment
#  Start with a number
location_data = 42.3601  # Latitude for Boston, MA

#  Assign a string to a variable
location_data = "Boston"

#  Assign a list to a variable
location_data = [42.3601, -71.0589]  # Latitude and Longitude for Boston, MA

print(location_data)  # Output: [42.3601, -71.0589]

# C. Naming Variables
# Variable names can contain letters, numbers, and underscores, but they cannot start with a number. They are case-sensitive and should be descriptive of the data they hold.
# Examples of valid variable names:
latitude = 42.3601
longitude = -71.0589
elevation = 147.2
city_name = "Boston"
population = 685094
coordinate_system = "WGS 84"

# Examples of invalid variable names:
x = 42.3601 # Too generic
data = "Boston" # Too vague
temp = 25.6 # Ambiguous - temperature or temporary?
l = [42.36, -71.06] # Single letter variables are hard to understand

# D. Variable Types
# Python has several built-in data types, including:
# 1. int: Integer numbers 
# These are whole numbers(e.g., 1, 42, -7)
num_features = 500 # Represents the number of features in a geospatial dataset

# 2. float: Floating-point numbers 
# These are numbers with a decimal point (e.g., 3.14, -2.5)
latitude = 35.6895 # Represents the latitude of a point on Earth's surface
longitude = 139.6917 # Represents the longitude of a point on Earth's surface

# 3. str: Strings 
# Strings are sequences of characters (e.g., "Hello, World!")
# Strings can be enclosed in single quotes ( ' ) or double quotes ( " ). You can also use triple quotes ( '''or """ ) for multiline strings.
coordinate_system = "WGS 84" # Represents a commonly used coordinate system

# 4. list: Ordered, mutable collections (e.g., [1, 2, 3])
# Lists are ordered collections of items, which can be of any data type.
coordinates = [
 35.6895,
 139.6917,
] # A list representing latitude and longitude of a point

# 5. tuple: Ordered, immutable collections (e.g., (1, 2, 3))
# Tuples are similar to lists, but they cannot be changed after they are created. They are often used to represent fixed collections of items.
point = (35.6895, 139.6917) # A tuple representing latitude and longitude of a point

# 6. dict: Key-value pairs (e.g., {"name": "Alice", "age": 30})
# Dictionaries are unordered collections of key-value pairs, where each key is unique. They are often used to represent structured data.
feature_attributes = {
 "name": "Mount Fuji",
 "height_meters": 3776,
 "type": "Stratovolcano",
 "location": [35.3606, 138.7274],
}

# 7. bool: Boolean values (True or False)
# Boolean values are used to represent truth values in logical operations. They can be used in conditional statements and loops.
is_georeferenced = True # Represents whether a dataset is georeferenced or not

# 8. NoneType: Represents the absence of a value (None)
# The NoneType is a special data type that represents the absence of a value or a null value. It is often used to indicate that a variable has not been assigned a value yet.
no_data_value = None # Represents a missing or undefined value in a dataset 

# E. Escaping Characters
# Escape characters are used to insert characters that are illegal in a string. For example, you can use the escape character \n to insert a new line in a string.
# In Python, you can use the backslash ( \ ) to escape special characters in strings. This allows you to include characters that would otherwise be interpreted differently by the Python interpreter.
print("Hello World!\nThis is a Python script.")

# Another common escape character is \t , which inserts a tab in a string
print("Hello World!\tThis is a Python script.")
print("This is the first line.\n\tThis is the second line. It is indented.")

# If you want to include a single quote in a string, you can wrap the string in double quotes
print("What's your name?")

# Alternatively, you can use the escape character \' to include a single quote in a string
print('What\'s your name?')

# F. Comments
# Comments are used to explain code and make it more readable. In Python, comments start with the hash symbol ( # ) and continue to the end of the line. Comments are ignored by the Python interpreter and do not affect the execution of the code.
# This is a comment
num_points = 120 # This is an inline comment

# G. Working with Variables And Data Types
# In Python, you can perform various operations on variables and data types. For example, you can perform arithmetic operations on numeric variables, concatenate strings, and manipulate lists and dictionaries.
# Adding a constant to the number of features:
num_features += 20
print("Updated number of features:", num_features)

# Converting latitude from degrees to radians (required for some geospatial calculations):
import math
latitude = 35.6895
latitude_radians = math.radians(latitude)
print("Latitude in radians:", latitude_radians) # We first import the math module, which contains the radians() function. Then we convert the latitude from degrees to radians.

# Adding new coordinates to the list of coordinates using the append() method:
coordinates = [35.6895, 139.6917]
coordinates.append(34.0522) # Adding latitude of Los Angeles
coordinates.append(-118.2437) # Adding longitude of Los Angeles
print("Updated coordinates:", coordinates)

# Accessing dictionary elements using the [] operator:
mount_fuji_name = feature_attributes["name"]
mount_fuji_height = feature_attributes["height_meters"]
print(f"{mount_fuji_name} is {mount_fuji_height} meters high.")

# H. Basic String Operations
# In Python, you can perform various operations on strings, such as concatenation, slicing, and formatting.
# Strings in Python come with many built-in methods that allow you to manipulate and format text data.
# This is particularly useful in geospatial work when dealing with place names, addresses, or data labels.
# Here are some common string operations:
# 1. Changing Case: You can change the case of a string using methods like upper(), lower(), and title().
city_name = "San Francisco"
# Convert to lowercase
city_lowercase = city_name.lower()
print("Lowercase:", city_lowercase)
# Convert to uppercase
city_uppercase = city_name.upper()
print("Uppercase:", city_uppercase)
# Convert to title case (first letter of each word capitalized)
city_title = city_name.title()
print("Title case:", city_title)

# 2. Replacing Substrings: You can replace parts of a string using the replace() method.
original_city = "San Francisco"
new_city = original_city.replace("San", "Los")
print("Original:", original_city)
print("Modified:", new_city)

# 3.  Other Useful String Methods
# Here are a few more string methods that are commonly used in geospatial programming:
location_data = " Mount Everest "
# Remove whitespace from beginning and end
clean_location = location_data.strip()
print("Cleaned:", clean_location)

# EXERCISE
# Exercise 1: Variable Assignment and Basic Operations
name_city = "New York"
latitude_ny = 40.7128  # Latitude for New York City
longitude_ny = -74.0060  # Longitude for New York City
population_ny = 8419600  # Population of New York City
areas_ny = 783.8  # Area of New York City in square kilometers

population_density_ny = population_ny / areas_ny  # Calculate population density
print(f"Population density of {name_city}: {population_density_ny:.2f} people per square kilometer.")

print(f"Latitude: {latitude_ny}, Longitude: {longitude_ny}") 

# Exercise 2: String Manipulation
city_name = "Los Angeles"
# Convert to uppercase
city_uppercase = city_name.upper()

# Convert to lowercase
city_lowercase = city_name.lower() 

print(f"City Name in Uppercase: {city_uppercase}")
print(f"City Name in Lowercase: {city_lowercase}")  

# Replace to Now York
new_city_name = city_name.replace("Los Angeles", "New York")
print(f"Replaced City Name: {new_city_name}")
