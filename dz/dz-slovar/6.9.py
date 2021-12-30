favorite_places = {
    'roma'  : ['moscow'],
    'maks' : ['kiev'],
    'igor'  : ['kharkov']
}

for name, places in favorite_places.items():
    print(f"{name.title()} Favorite places is:")
    for place in places:
        print( place.title())
