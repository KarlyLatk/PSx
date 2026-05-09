class Student:
    def __init__(self, first, last, code, credits):
        self.first = first
        self.last = last
        self.code = code
        self.credits = credits

    def tuition_owed(self):
        #compare the value within the given code
        tuition = code_dictionary.get(self.code)
        #based on that, multiply it by the credits
        return float(tuition) * float(self.credits)

code_dictionary = {
    "I": 250,
    "O": 500,
    "X": 800,
    "G": 250
}
stud1 = Student('Karly', 'Latkiewicz', 'I', 4)
stud2 = Student('Bob', 'Smith', 'O', 3)
stud3 = Student('Martha', 'White', 'G', 4)
stud4 = Student('Aveline', 'Rigatoni', 'X', 3)

print(stud1.first," ", stud1.last, " ", stud1.tuition_owed())
print(stud2.first," ", stud2.last, " ", stud2.tuition_owed())
print(stud3.first," ", stud3.last, " ", stud3.tuition_owed())
print(stud4.first," ", stud4.last, " ", stud4.tuition_owed())