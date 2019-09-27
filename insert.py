import random
import time

class Student:
    def __init__(self, last, first, ssn, email, age):
        self.mLast = last
        self.mFirst = first
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age

    def getStudentInfo(self):
        newStr = str(self.mLast) + " " + str(self.mFirst) + " " +  str(self.mSSN) + " " +  str(self.mEmail) + " " +  str(self.mAge)
        return newStr

    def getSSN(self):
        return self.mSSN

def createStudentObjects():

    start = time.time()

    studentObjList = []

    fin = open("InsertNames.txt", "r")
    for line in fin:
        newLine = line.split()
        duplicate = False
        for obj in studentObjList:
            if obj.getSSN() == newLine[2]:
                duplicate = True
        if duplicate:
            print(line.strip() + ": " + " is a duplicate student. Not added to student list.")
        else:
            student = Student(newLine[0], newLine[1], newLine[2], newLine[3], newLine[4])
            studentObjList.append(student)
    fin.close()

    stop = time.time()
    total = stop - start
    print("It took the program " + str(total) + "seconds to finish.")

createStudentObjects()
