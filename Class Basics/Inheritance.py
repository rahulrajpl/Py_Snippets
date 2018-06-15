class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + "," + self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    grade = None

    def __init__(self, firstName, lastName, idNumber, scores = []):
        #Person.__init__(self,firstName, lastName, idNumber)
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        avg_score = sum(self.scores)/len(self.scores)

        if avg_score >= 90 and avg_score < 101:
            self.grade = 'O'
        elif avg_score >= 80 and avg_score < 91:
            self.grade = 'E'
        elif avg_score >= 70 and avg_score < 81:
            self.grade = 'A'
        elif avg_score >= 55 and avg_score < 71:
            self.grade = 'P'
        elif avg_score >= 40 and avg_score < 56:
            self.grade = 'D'
        elif avg_score < 40:
            self.grade = 'T'
        return self.grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, input().split()))
print(len(scores))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
