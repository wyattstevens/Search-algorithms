import random
import time


def createList(size, low, high):

    myList = []

    for i in range(size):
        myList.append(random.randrange(low, high+1))

    return myList

def bubbleSort(myList):

    switched = True

    while switched:
        switched = False

        for i in range(len(myList)-1):

            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
                switched = True


def shakerSort(myList):

    switched = True

    while switched:
        switched = False

        for i in range(len(myList)-1):

            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
                switched = True

        for i in range(len(myList)-2, 0, -1):

            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
                switched = True


def selectionSort(myList):


    for i in range(len(myList)-1):

        min_index = i

        for j in range(i+1, len(myList)):

            if myList[min_index] > myList[j]:
                min_index = j
        myList[i], myList[min_index] = myList[min_index], myList[i]


def mergeSort(myList):

    if len(myList) <= 1:
        return myList

    middle = len(myList) // 2

    leftList = myList[:middle]
    rightList = myList[middle:]

    mergeSort(leftList)
    mergeSort(rightList)

    i = j = k = 0

    while ( i < len(leftList) and j < len(rightList) ):
        if leftList[i] < rightList[j]:
            myList[k] = leftList[i]
            i += 1
        else:
            myList[k] = rightList[j]
            j += 1
        k += 1

    while ( i < len(leftList) ):
        myList[k] = leftList[i]
        i += 1
        k += 1

    while ( j < len(rightList) ):
        myList[k] = rightList[j]
        j += 1
        k += 1
        

def main():

    myList = createList(10, 0, 10)
    myList2 = myList[:]
    myList3 = myList[:]
    myList4 = myList[:]


    print(myList)
    bubbleSort(myList)
    print(myList)

    print("\n\n")

    print(myList2)
    shakerSort(myList2)
    print(myList2)

    print("\n\n")

    print(myList3)
    selectionSort(myList3)
    print(myList3)

    print("\n\n")

    print(myList4)
    mergeSort(myList4)
    print(myList4)

    return 0


main()
