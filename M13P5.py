def class_average(dictionary):
    exam1_total = 0.0
    exam2_total = 0.0
    exam3_total = 0.0
    length = len(dictionary)

#access each index location [0]
#for each location add it to that location and get the average
    for key, value in dictionary.items():
        exam1_total += float(value[0])
        exam2_total += float(value[1])
        exam3_total += float(value[2])

    average_1 = exam1_total/length
    average_2 = exam2_total/length
    average_3 = exam3_total/length

    print("Average exam 1: ", round(average_1,2))
    print("Average exam 2: ", round(average_2,2))
    print("Average exam 3: ", round(average_3,2))

def student_average(dictionary):
    total = 0.0
    for key, value in dictionary.items():
        total = float(value[0]) + float(value[1]) + float(value[2])
        average = total/3
        print("{: >20} {: >20}".format(f"{key}", round(average,2)))

dictionary_student = {
    "Karly": [80, 76.2, 98.4],
    "Kevin": [90, 56.5, 75,8],
    "George": [75, 75.9, 54.8],
    "Aveline": [56, 43.1, 78.3],
    "Cassandra": [99, 96.7, 98.9],
    "Fred": [45, 75.3, 80],
    "Layla": [68, 54.5, 60],
    "Rowan": [74, 83.4, 75.8],
    "Joan": [96, 76.9, 80.3],
    "James": [78, 86.4, 91.3]
}
print("Class 101: ")
print("{: >20} {: >20}".format('Student:', 'Average:'))
student_average(dictionary_student)
print("Class Average: ")
class_average(dictionary_student)
