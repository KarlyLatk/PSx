class Student:
    def __init__(self, first, last, code, credits):
        self.first = first
        self.last = last
        self.code = code
        self.credits = credits

    def tuition_owed(self):
        if self.code.lower() == 'i':
            o = float(self.credits) * 250
            return o
        o = float(self.credits) * 500
        return o

stud1 = Student('Karly', 'Latkiewicz', 'i', 4)
stud2 = Student('Bob', 'Smith', 'o', 3)

print(stud1.first," ", stud1.last, " ", stud1.tuition_owed())
print(stud2.first," ", stud2.last, " ", stud2.tuition_owed())