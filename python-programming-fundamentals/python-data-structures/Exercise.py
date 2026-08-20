# 1. Exercise Using 
# Dataset
cities = [
    (40.7128, -74.0060),  # New York City
    (34.0522, -118.2437), # Los Angeles
    (41.8781, -87.6298),  # Chicago
]

# Add a new city to the list 
cities.append((25.7617, -80.1918))  # Miami
print("City List:", cities)

# Slice the list to print only the first two cities
first_two_cities = cities[:2]
print("First Two Cities:", first_two_cities)

# 2. Exercise Using Tuples
# Dataset
eiffel_tower_point = (48.8584, 2.2945)  # Eiffel Tower coordinates

# Access the latitude and longitude from the tuple
latitude = eiffel_tower_point[0]
longitude =  eiffel_tower_point[1]

print(f"Eiffel Tower located at {latitude}°N, {longitude}°E")

# Try to change the latitude value (this will raise an error)
# eiffel_tower_point[0] = 48.8585  # Attempt to change 

# 3. Exercise Using Sets
# Dataset
visited_countries = {"USA", "France", "Germany"}
print("Original Set of Visited Countries:", visited_countries)

# Add a new country to the set
visited_countries.add("Italy")
print("Updated Set of Visited Countries:", visited_countries)

# Try to add a duplicate country (this will not change the set)
visited_countries.add("France")
print("Set of Visited Countries (after adding duplicate):", visited_countries)

# 4. Exercise Using Dictionaries
# Dataset
river_info = {
    "name": "Amazon River",
    "length_km": 6400,
    "countries": ["Brazil", "Peru", "Colombia"]
}

# Add a new key-value pair to the dictionary
river_info["discharge_m3_per_s"] = 209000

# Update the length of the river
river_info["length_km"] = 6992

print("Updated River Info:", river_info)

# 5. Exercide with Nested Data Structures
# Dataset
tokyo_info ={
    "name": "Tokyo",
    "population": 13515271,
    "coordinates":(35.6895,139.6917),
}

# Access city population
city_population = tokyo_info["population"]
print("Tokyo Population is:", city_population)

# Access city latitude and longitude
city_coordinates = tokyo_info["coordinates"]
latitude = city_coordinates[0]
longitude = city_coordinates[1]
print(f"Tokyo located at {latitude}°N, {longitude}°E")

# Update Population
tokyo_info["population"] = 14000000
print("Updated Tokyo Info:", tokyo_info)