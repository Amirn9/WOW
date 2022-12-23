superheroes = [
    {'name': 'Superman', 'lovely': 8},
    {'name': 'Wonder Woman', 'lovely': 9},
    {'name': 'Hulk', 'lovely': 5},
    {'name': 'Thor', 'lovely': 7},
    {'name': 'Iron Man', 'lovely': 6},
    {'name': 'Captain America', 'lovely': 10},
    {'name': 'Black Widow', 'lovely': 9},
    {'name': 'Hawkeye', 'lovely': 6},
    {'name': 'Black Panther', 'lovely': 8},
    {'name': 'Spider-Man', 'lovely': 7},
]

# Sort the list of superheroes by loveliness
sorted_superheroes = sorted(superheroes, key=lambda x: x['lovely'], reverse=True)

# Print the top 10 most lovely superheroes
for i in range(10):
    print(f"{i+1}. {sorted_superheroes[i]['name']}")