### INTRODUCTION TO PYTHON DATA STRUCTURES ###

# Data structures are the building blocks that allow us to organize and store multiple pieces of related information together. 
# While individual variables hold single values like a coordinate or place name, data structures let us group multiple values in meaningful ways. 
# This becomes essential in geospatial programming where we often work with collections of coordinates, lists of place names, sets of unique identifiers, and structured attribute information.
# Python provides several built-in data structures that are particularly useful for geospatial work: tuples for storing fixed coordinate pairs, lists for sequences of locations along a path, sets for collections of unique identifiers, and dictionaries for organizing feature attributes. 
# Understanding when and how to use each of these structures is fundamental to effective geospatial programming.
# These data structures serve as the foundation for more complex geospatial operations. 
# Whether you’re tracking a GPS route with a list of coordinates, storing unique country codes in a set, or organizing feature attributes in a dictionary, mastering these basic structures will enable you to work efficiently with spatial data.



### TUPLES ###

# Tuples are immutable sequences, which means that once a tuple is created, you cannot change, add, or remove its elements. 
# This immutability makes tuples perfect for storing data that should remain constant throughout your program’s execution. In geospatial programming, tuples are commonly used to represent coordinate pairs, since a point’s latitude and longitude typically shouldn’t change once defined. 
# The immutable nature of tuples provides several advantages: they’re memory-efficient, can be used as dictionary keys (which we’ll see later), and help prevent accidental modification of important spatial reference data. 
# When you want to represent a fixed geographic location, a tuple is often the best choice.

# 1. Creating and Using Tuples
# Tuples are created using parentheses () with elements separated by commas. 
# Let’s create a tuple to represent the coordinates of Tokyo:

tokyo_points = (35.6895,
                139.6917,
                ) # Tuple representing Tokyo's coordinates (latitude, longitude)

print (f"Tokyo Coordinates: {tokyo_points}") # Output: Tokyo Coordinates: (35.6895, 139.6917)

# 2. Accessing Tuple Elements
# You can access elements in a tuple using indexing, where the first element has an index of 0.

latitude = tokyo_points[0]
longitude = tokyo_points[1]
print (f"Latitude:{latitude}")
print (f"longitude:{longitude}")

# 3. Tuple Unpacking
# Python allows you to unpack tuples into individual variables, which can make your code cleaner and more readable.

lat , lon = tokyo_points
print (f"Tokyo is located at {lat}°N, {lon}°E") # Output: Tokyo is located at 35.6895°N, 139.6917°E

# 4. Multiple Tuples
# You can create multiple tuples to represent different geographic locations.

# Different geographic locations represented as tuples
new_york = (40.7128, -74.0060) # New York City coordinates
london = (51.5074, -0.1278) # London coordinates
sydney = (-33.8688, 151.2093) # Sydney coordinates

print (f"New York Coordinates:{new_york}")
print (f"London Coordinates:{london}")
print (f"Sydney Coordinates:{sydney}")
