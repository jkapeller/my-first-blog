def ricksanchez(name):
    if name=='Morty' or name=='Birdman':
        print("Hey " + name + "\n" + "Help, I'm in great pain.")
    else:
        print("Hey " + "*burp* " + name + "\n" +  "Wubba lubba dub dub!")

peopleFromEarthDimensionC134 = ['Morty', 'Gearman', 'Squanchy', 'Birdman', 'Beth', 'Summer', 'Jerry']

def greet(people):
    for name in people:
        ricksanchez(name)

greet(peopleFromEarthDimensionC134)