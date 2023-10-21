import sqlite3

# Connect to the database
conn = sqlite3.connect('cities.db')

from tabulate import tabulate

data = ["Pretoria", "Johannesburg", "Sandton","Midrand","Mamelodi","Steyn city","Cosmo city"]
data = [int( 5000000), int( 5000000), int( 5000000),int( 5000000),int( 5000000),int( 5000000),int( 5000000)]
headers = ["city", "population"]

print(tabulate(data, headers=headers))
# Create the Cities table if it doesn't exist
cursor = conn.cursor()
cursor.execute('''from tabulate import tabulate

data = [["Pretoria", 5000000], ["Johannesburg", 3000000], ["Sandton", 3000005]["Midrand", 3200005]["Mamelodi",250000["Steyn city",2650000]["Cosmo city",5000402]]]
headers = ["city", "population"]

print(tabulate(data, headers=headers))
                )''')

# Function to display a list of cities sorted by population in ascending order
def display_cities_sorted_by_population_ascending():
    cursor.execute('SELECT * FROM Cities ORDER BY Population ASC')
    cities = cursor.fetchall()
    for city in cities:
        print(city)

# Function to display a list of cities sorted by population in descending order
def display_cities_sorted_by_population_descending():
    cursor.execute('SELECT * FROM Cities ORDER BY Population DESC')
    cities = cursor.fetchall()
    for city in cities:
        print(city)

# Function to display a list of cities sorted by name
def display_cities_sorted_by_name():
    cursor.execute('SELECT * FROM Cities ORDER BY CityName')
    cities = cursor.fetchall()
    for city in cities:
        print(city)

# Function to display the total population of all the cities
def display_total_population():
    cursor.execute('SELECT SUM(Population) FROM Cities')
    total_population = cursor.fetchone()[0]
    print('Total population:', total_population)

# Function to display the average population of all the cities
def display_average_population():
    cursor.execute('SELECT AVG(Population) FROM Cities')
    average_population = cursor.fetchone()[0]
    print('Average population:', average_population)

# Function to display the city with the highest population
def display_city_with_highest_population():
    cursor.execute('SELECT CityName FROM Cities ORDER BY Population DESC LIMIT 1')
    city = cursor.fetchone()[0]
    print('City with highest population:', city)

# Function to display the city with the lowest population
def display_city_with_lowest_population():
    cursor.execute('SELECT CityName FROM Cities ORDER BY Population ASC LIMIT 1')
    city = cursor.fetchone()[0]
    print('City with lowest population:', city)

# Main program loop
while True:
    print('1. Display a list of cities sorted by population, in ascending order.')
    print('2. Display a list of cities sorted by population, in descending order.')
    print('3. Display a list of cities sorted by name.')
    print('4. Display the total population of all the cities.')
    print('5. Display the average population of all the cities.')
    print('6. Display the city with the highest population.')
    print('7. Display the city with the lowest population.')
    
    choice = input('\nEnter your choice (1-7): ')
    
    if choice == '1':
        display_cities_sorted_by_population_ascending()
        
    elif choice == '2':
        display_cities_sorted_by_population_descending()
        
    elif choice == '3':
        display_cities_sorted_by_name()
        
    elif choice == '4':
        display_total_population()
        
    elif choice == '5':
        display_average_population()
        
    elif choice == '6':
        display_city_with_highest_population()
        
    elif choice == '7':
        display_city_with_lowest_population()
        
    else:
        break

# Close the connection
conn.close()