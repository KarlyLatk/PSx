def display_grades(last_name, exam_score):
    greatest = 0
    lowest = 999

    position_greatest = 0
    position_lowest = 0
    for scores in exam_score:
        if scores > greatest:
            greatest = scores
            position_greatest = exam_score.index(scores)

        if scores < lowest:
            lowest = scores
            position_lowest = exam_score.index(scores)

    print(last_name[position_greatest], greatest)
    print(last_name[position_lowest], lowest)


last_name = []
exam_score = []
with open('exam_scores.txt') as f:
    i = 1
    lines = f.readlines()
    for line in lines:
        if i % 2 == 0:
            #even - exam scores
            score = int(line)
            exam_score.append(score)
        else:
            #odd
            last_name.append(line)
        i+=1

display_grades(last_name, exam_score)
f.close()

