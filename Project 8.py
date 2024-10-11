subjects = []
grades = []
for i in range (0,3):
    subjects.append (input("Give me a subject: "))
    grades.append (input("Give me the grade: "))


for x in range (0,3):
    print (subjects [x] + " has grade : " + grades [x])
    #print (f"{subjects [x]} has grade: {grades [x]}" )
