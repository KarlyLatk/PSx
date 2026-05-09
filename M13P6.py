def dictionary_contents(dictionary):
    print("{: >20} {: >20}".format('Player:', 'Batting Average:'))
    for key, value in dictionary.items():
        print("{: >20}".format(f"{key}"), "{: >20}".format(f"{value}"))


with open('Baseball_team1.txt') as f:
    my_dictionary = dict(line.strip().split(': ') for line in f)

dictionary_contents(my_dictionary)

f.close()

