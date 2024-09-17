students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"}, #none is a thing in python that means no value in dictionary terms 
]

for student in students:
    print (student["name"], "is in", student["house"], "and has a patronus of", student["patronus"]) #student["name"] is the value of the key name in the dictionary student etc.