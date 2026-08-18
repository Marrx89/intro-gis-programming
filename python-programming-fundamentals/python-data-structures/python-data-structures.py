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


### LIST ###
# Lists are ordered, mutable sequences that can store multiple items in a single container. 
# Unlike tuples, lists are mutable, which means you can change, add, or remove elements after the list has been created. 
# This flexibility makes lists incredibly useful for geospatial applications where you need to build collections of data dynamically, such as tracking a GPS route, storing elevation measurements along a transect, or maintaining a collection of waypoints. 
# Lists maintain the order of elements, which is crucial for geospatial applications where sequence matters. 
# For example, when representing a path or route, the order of waypoints determines the direction of travel.
# Lists can store different types of data (numbers, strings, tuples, or even other lists), making them versatile containers for complex geospatial information.

# 1. Creating Lists
# Lists are created using square brackets [] with elements separated by commas. 
# Here are some examples relevant to geospatial work:

# A list of coordinate tuples representing a travel route
route = [
    (35.6895, 139.6917),    # TOKYO
    (34.0522, -118.2437),   # LOS ANGELES
    (51.5074, -0.1278),     # LONDON
]
print ("Travel Route:", route)

# A list of elevation measurements (in meters)
elevations = [120.5, 130.2, 125.0, 140.8, 135.6]
print ("Elevation Profile:", elevations)

# A list of city names
cities = ["Tokyo", "Los Angeles", "London", "Paris"]
print("Cities to visit:", cities)

# 2. Adding elements to Lists
# One of the key advantages of lists is the ability to add new elements dynamically using the append() method. 
# This is particularly useful when you need to build a list of coordinates or other data points as you process them.

# Add Paris to our travel route
route.append((48.8566, 2.3522)) # Paris coordinate
print ("Updated Route:", route)

# Add a new elevation measurement
elevations.append(221.4)
print("Updated Elevations:", elevations)

# Note that the append() method modifies the list in place, meaning it directly changes the original list rather than returning a new list.

# 3. Accessing List Elements
# You can access individual elements using indexing (starting from 0) or retrieve multiple elements using slicing:

# Accessing the first city our route
first_stop = route[0]
print (f"First stop:{first_stop}")

# Accessing the last city using negative indexing
last_city = route[-1]
print(f"Last city:{last_city}")

# 4. Slicing Lists
# Slicing allows you to extract portions of a list, which is useful for analyzing segments of routes or data:

# Get the first two stops of our route
first_two_stops = route [:2]
print ("First two stops:", first_two_stops)

# Get the last two stops of our route
last_two_stops = route[-2:]
print ("Last two stops:", last_two_stops)

# Get the middle stop of elevation data     
middle_elevations = elevations[2:5]
print ("Middle elevations:", middle_elevations) 

# 5. Usefull List Operations
# Lists provide many helpful methods for working with geospatial data, such as finding the number of waypoints in a route, calculating the highest elevation, or computing the average elevation. 
# These opera￾tions are essential for analyzing and visualizing geospatial data.

# Find the number of waypoints in our route
num_waypoints = len(route)
print(f"Number of waypoints:{num_waypoints}")

# Find the highest elevation
max_elevations = max(elevations)
print(f"Highest elevation:{max_elevations} meters")

# Compute the average elevation
avg_elevation = sum(elevations) / len(elevations)
print(f"Average elevation:{avg_elevation:.1f} meters")
