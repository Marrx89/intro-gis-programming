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



### SETS ###
# Sets are unordered collections of unique elements, meaning they automatically eliminate duplicates and don’t maintain any particular order. 
# This makes sets incredibly useful in geospatial programming when you need to work with unique identifiers, remove duplicate entries from datasets, or perform operations like finding common elements between different spatial datasets.
# Sets are particularly valuable when working with categorical spatial data. 
# For example, you might want to track unique country codes in a global dataset, identify distinct land cover types in a study area, or maintain a collection of unique coordinate system identifiers. 
# The automatic duplicate removal feature of sets saves you from having to manually check for and remove repeated values.

# 1. Creating Sets
# You can create sets in several ways. 
# You can use curly braces {} to create a set, or use the set() function to convert a list or other iterable into a set. 
# Here are examples relevant to geospatial work:

# Create a sets of geographic region
region_visited = {"North America", "Europe", "Asia"}
print("Regions Visited:", region_visited)

# Create a set of unique country codes from a list (automatically removes duplicates)
country_codes = ["US", "CA", "MX", "US", "CA"]
unique_codes = set(country_codes)
print("Original list:", country_codes)
print("Unique country codes:", unique_codes)

# Create a set of coordinate system codes
crs_codes = {"EPSG:4326", "EPSG:3857", "EPSG:32633"}
print("Coordinate Reference System:", crs_codes)

# 2. Adding Elements to Sets
# You can add new elements to a set using the add() method.
# Duplicates will be automatically ignored.

# Add a new region to our visited set
print("Original set:", region_visited)
region_visited.add("South America")
print("Set after adding a new region:", region_visited)

# Try to add a duplicate region (will be ignored)
region_visited.add("Europe")
print("Set after attempting to add a duplicate region:", region_visited)

# 3. Removing Elements from Sets
# You can remove elements from a set using the remove() method.
# If the element does not exist, remove() will raise a KeyError.
# region_visited.remove("Asia")
# print("Set after removing 'Asia':", region_visited)

# To avoid this, you can use the discard() method, which will not raise an error if the element is not found.
# region_visited.discard("South America") 
# print("Set after discarding 'South America':", region_visited)

# 4. Set Practical Operations
# Sets provide useful operations for comparing different spatial datasets. 
# For example, you might want to find the common countries between two different datasets, or identify the unique countries in a dataset. 
# The intersection() method returns a set of elements that are common to both sets, while the union() method returns a set of all elements from both sets.
# The difference() method returns a set of elements that are in one set but not in the other.
# Here the examples:

# Two different survey areas with their observed species
area_a_species = {"Deer", "Fox", "Rabbit", "tiger"}
area_b_species = {"Rabbit", "Bear", "Wolf", "Deer"}

print("Species in Area A:", area_a_species)
print("Species in Area B:", area_b_species)

# Find common species between the two areas
common_species = area_a_species.intersection(area_b_species)
print("Species found in both areas:", common_species)

# Find species unique to Area A
unique_to_area_a = area_a_species.difference(area_b_species)
print("Species only in Area A:", unique_to_area_a)

# Find species unique to Area B
unique_to_area_b = area_b_species.difference(area_a_species)
print("Species only in Area B:", unique_to_area_b)    

# Find all species across both areas
all_species = area_a_species.union(area_b_species)
print("All species found:", all_species)

# 5. Set Membership Testing
# Sets provide a fast way to test for membership, which is useful when checking if a particular identifier or value exists in a dataset.

# Check if we've visited a particular region
if "Asia" in region_visited:
    print("We have visited Asia.")

if "Africa" in region_visited:
    print("We have visited Africa.")
else:       
    print("We have not visited Africa.")



### DICTIONARIES ###
# Dictionaries are collections of key-value pairs where each key is unique and maps to a specific value. 
# This structure is perfect for storing related information about geographic features, where you need to associate descriptive attributes with specific identifiers. 
# In geospatial programming, dictionaries are extensively used to store feature attributes, metadata about datasets, configuration settings, and any situation where you need to organize information by meaningful names rather than numeric positions. 
# Think of dictionaries as lookup tables or filing systems where you can quickly find information using a descriptive key. 
# For example, instead of remembering that population data is stored in position 2 of a list, you can simply use the key “population” to access that information directly. 
# This makes your code more readable and less prone to errors.

# 1. Creating Dictionaries
# Dictionaries are created using curly braces {} with key-value pairs separated by commas and keys separated from values by colons.
# Here are some examples relevant to geospatial work:

# Dictionary storing attributes of a city
new_york_info = {
    "name" : "New York City",
    "population" : 8419600,
    "coordinates" : (40.7128, -74.0060),
    "country" : "USA",
    "established" : 1624,
}
print("New York City Info:", new_york_info)

# Dictionary for geographic survey point
survey_point = {
    "id" : "SP001",
    "latitude" : 34.0522,
    "longitude" : -118.2437,
    "elevation" : 89.0,
    "land_cover" : "Urban",
    "date_surveyed" : "2023-05-15",
    "description" : "Survey point in Los Angeles",
}
print("Survey Point Info:", survey_point)

# 2. Accessing Dictionary Values
# You can access values in a dictionary using their corresponding keys in square brackets or with the get() method.

# Accessing specific infromation about New York City
city_name = new_york_info["name"]
city_population = new_york_info.get("population")   
city_coordinates = new_york_info["coordinates"]
print(f"{city_name} has a population of {city_population} and is located at coordinates {city_coordinates}.")

# Keep in mind that if you try to access a key that doesn’t exist in a dictionary, you’ll get a KeyError error. 
# To avoid this, you can use the get() method as introduced below to safely access a key and provide a default value if the key doesn’t exist.

# 3. Safe Acces with get() Method
# The get() method allows you to access a value associated with a key while providing a default value if the key is not found. 
# This is particularly useful when working with datasets that may have missing attributes.

# Safe access to dictionary value
area = new_york_info.get("area_km2", "Area information not available")
timezone = new_york_info.get("timezone", "Timezone information not available")

print(f"Area:{area}")
print(f"Timezone:{timezone}")

# 4. Adding and Updating Values
# You can add new key-value pairs or update existing ones.

# Add new information to our New York Dictionary
new_york_info["area_km2"] = 783.8 # Adding area in square kilometers
new_york_info["timezone"] = "Eastern Standard Time" # Adding timezone information
new_york_info["population"] = 8500000 # Updating population information
print("Updated New York City Info:", new_york_info)

# 5. Working with Geographic Feature Collection
# Dictionaries can also be used to represent collections of geographic features, where each feature is identified by a unique key (like an ID) and its attributes are stored as a nested dictionary.

# Collection of world capital
world_capitals = {
    "Japan" : {
        "capital" : "Tokyo",
        "coordinates" : (35.6895, 139.6917),
        "population" : 13929286,
    },
    "USA" : {
        "capital" : "Washington, D.C.",
        "coordinates" : (38.9072, -77.0369),
        "population" : 705749,
    },
    "France" : {
        "capital" : "Paris",
        "coordinates" : (48.8566, 2.3522),
        "population" : 2140526,
    },
    "UK" :{
        "capital" : "London",
        "coordinates" : (51.5074, -0.1278),
        "population" : 8982000,
    },
}
# Access information about a specific capital
UK_capital_info = world_capitals["UK"]
print(f"UK capital: {UK_capital_info['capital']}, Coordinates: {UK_capital_info['coordinates']}, Population: {UK_capital_info['population']}")

# As you can see from the example above, a dictionary can be nested within another dictionary. 
# This is useful when you need to store information about a city, and then store information about the city’s population, coordinates, and country.

