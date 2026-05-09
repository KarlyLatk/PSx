def display_names(last_name, exam_score):
    for names in range(0, len(last_name)):
        print(last_name[names], end=", ")
        print(exam_score[names])

def display_reverse(last_name, exam_score):
    for names in range(1, len(last_name)+1):
        print(last_name[len(last_name)-names], end=", ")
        print(exam_score[len(exam_score)-names])

last_name = ["Latkiewicz", "Smith", "Engstrom", "Parker", "Farma", "White", "Orces", "Jones", "Williams", "Albert"]
exam_score = [80, 75, 100, 60, 99, 101, 87, 35, 55, 78]
print("Regular: ")
display_names(last_name, exam_score)
print("Reverse: ")
display_reverse(last_name, exam_score)