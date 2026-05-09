dictionary_student = {
    "Karly": 80,
    "Kevin": 90,
    "George": 75,
    "Aveline": 56,
    "Cassandra": 99,
    "Fred": 45,
    "Layla": 68,
    "Rowan": 74,
    "Joan": 96,
    "James": 78
}
total = 0.0
print("{: >20} {: >20}".format('Student', 'Grade'))
for key, value in dictionary_student.items():
    print("{: >20}".format(f"{key}"), "{: >20}".format(f"{value}"))

for key, value in dictionary_student.items():
    total += float(value)

print ("Average: ", total/len(dictionary_student))

