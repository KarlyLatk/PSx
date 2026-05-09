def display_names(last_name):
    print(last_name)

def display_reverse(last_name):
    for names in range(1, len(last_name)+1):
        print(last_name[len(last_name)-names], end=" ")

last_name = ["Latkiewicz", "Smith", "Engstrom", "Parker", "Farma", "White", "Orces", "Jones", "Williams", "Albert"]

display_names(last_name)

display_reverse(last_name)

