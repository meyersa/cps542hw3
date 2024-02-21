# August Meyers
# CPS 542 Ahmet Uger
# HW3
#
# arg[1] data file name
# arg[2] output file name
# arg[3] max array size
# arg[4] print flag
# arg[5] chart flag
# arg[6] compare flag
#
# Takes in a data file and sorts it with 7 algorithms while recording the time
# Doesn't count since that takes too much time
# Also might not work on O(n^2) algorithms over a certain amount of times due to time complexity

import datetime
import sys

# Hits recursion limit
sys.setrecursionlimit(10000000)

swapCount = 0
compareCount = 0


def main():

    # Restate as global so they can be written to
    global inputFile
    global inputOut
    global inputMax
    global inputPrint

    # Output lists
    timeList = {}
    sortedList = {}
    swapList = {}
    compareList = {}

    # List of all algorithms (function name)
    algorithms = ["radixSort", "heapSort", "quickSortHelper",
                  "mergeSort", "insertionSort", "selectionSort", "bubbleSort"]

    # Read in CLI args
    try:
        inputFile = sys.argv[1]
        inputOut = sys.argv[2]
        inputMax = int(sys.argv[3])

    # Error with CLI args
    except:
        print("There was an error with your inputs. \n" + \
              "Please make sure you include [file name] [output file name] [max array size] [opt: print flag]")
        return

    # Set print flag
    try:
        inputPrint = sys.argv[4]

    except:
        inputPrint = 0

    # Set chart flag
    try:
        inputChart = sys.argv[5]

    except:
        inputChart = 0

    # Set compare flag
    try:
        inputCompare = sys.argv[5]

    except:
        inputCompare = 0

    # Opening print statement
    print("meyer4a -- August Meyers -- CPS542 HW3")

    # Clean output file
    with open(inputOut, 'w') as f:
        f.write("HW3 File Output\n")

    # Call all functions
    for alg in algorithms:
        sortCaller(alg, timeList, sortedList, swapList, compareList)

    # If compare flag is set
    if (inputCompare):
        compareResults(sortedList)

    # If chart flag is set
    if (inputChart):
        outputChart(timeList, swapList, compareList)


def bubbleSort(arr):
    global swapCount
    global compareCount

    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            compareCount += 1

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapCount += 1
                swapped = True
        if swapped == False:
            break


def selectionSort(arr):
    global swapCount
    global compareCount

    for i in range(len(arr)):

        min_idx = i
        for j in range(i + 1, len(arr)):

            compareCount += 1
            if arr[min_idx] > arr[j]:
                min_idx = j

        swapCount += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertionSort(arr):
    global swapCount
    global compareCount

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            compareCount += 1
            arr[j + 1] = arr[j]
            j -= 1

        swapCount += 1
        arr[j + 1] = key


def mergeSort(arr):
    global swapCount
    global compareCount

    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]

        R = arr[mid:]

        mergeSort(L)

        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            compareCount += 1

            if L[i] <= R[j]:
                swapCount += 1
                arr[k] = L[i]
                i += 1
            else:
                swapCount += 1
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            swapCount += 1

            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            swapCount += 1

            arr[k] = R[j]
            j += 1
            k += 1


def quickSort(arr, low, high):
    global swapCount
    global compareCount

    if low < high:
        compareCount += 1

        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] <= pivot:
                compareCount += 1

                i = i + 1

                (arr[i], arr[j]) = (arr[j], arr[i])
                swapCount += 1

        (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
        swapCount += 1

        pi = i + 1

        quickSort(arr, low, pi - 1)

        quickSort(arr, pi + 1, high)


def quickSortHelper(arr):
    return quickSort(arr, 0, len(arr) - 1)


def heapify(arr, N, i):
    global swapCount
    global compareCount

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        compareCount += 1

        largest = l

    if r < N and arr[largest] < arr[r]:
        compareCount += 1

        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        swapCount += 1

        heapify(arr, N, largest)


def heapSort(arr):
    global swapCount
    global compareCount

    N = len(arr)

    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        swapCount += 1

        heapify(arr, i, 0)


def radixSort(arr):
    global swapCount
    global compareCount

    max1 = max(arr)

    exp = 1
    while max1 / exp >= 1:
        compareCount += 1

        n = len(arr)

        output = [0] * (n)

        count = [0] * (10)

        for i in range(0, n):
            index = arr[i] // exp
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            compareCount += 1

            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]

        exp *= 10

# Helper func to read in the files


def openFile(fileName):
    output = []

    with open(fileName) as f:
        for line in f.readlines():
            try:
                output.append(int(line))

            except:
                continue

    return output

# Helper func to print the results out to files


def printToFile(arr, sort, time):
    with open(inputOut, 'a') as f:
        f.write(f'\nAlgorithm: {sort} | Time: {time}\n')

        for line in arr:
            f.write(str(line) + "\n")

# Helper func to call all the functions


def sortCaller(sort, timeList, sortedList, swapList, compareList):
    global swapCount
    global compareCount

    # Reset counters
    swapCount = 0
    compareCount = 0

    # Basic print
    print(f'\nAlgorithm: {sort}')

    # Open array with max
    arr = openFile(inputFile)[:inputMax]

    # Print arr if flag is set
    if (inputPrint == 1):
        print(f'Data File: {inputFile}, BEFORE SORTING: {arr}')

    # Start timer
    startTime = datetime.datetime.now()

    # Call func using globals
    globals()[sort](arr)

    # End and collect time
    timeList[sort] = datetime.datetime.now() - startTime

    # Save counts
    swapList[sort] = swapCount
    compareList[sort] = compareCount

    # Save arr
    sortedList[sort] = arr

    # Print arr if flag is set
    if (inputPrint == 1):
        print(f'Data File: {inputFile}, AFTER SORTING: {arr}')

    # Save arr to file
    printToFile(arr, sort, timeList[sort])

    print(f"Time: {timeList[sort]}")

# Compares each array to the first one to find differences
# Prints difference if it finds it


def compareResults(sortedList):
    flag = {}

    zero = list(sortedList.keys())[0]

    for s in list(sortedList.keys())[1:]:
        flag[s] = 0

        for i in range(len(sortedList.get(s))):
            if sortedList.get(zero)[i] != sortedList.get(s)[i]:
                flag[s] = 1
    flagval = 0 

    for f in flag.keys():
        if flag[f] == 1:
            flagval = 1

    if (flagval == 0):
        print("\nComparison found no issues\n")

    else: 
        print("\nComparison found errors\n")


def outputChart(timeList, swapList, compareList):
    print("\n\nChart of time comparisons\n")
    print(f'{"Name": <20}{"Time": <20}{"Swaps": <10}{"Comparisons": <10}')
    for alg in timeList.keys():
        print(f'{alg: <20}{str(timeList[alg]): <20}{swapList[alg]: <10}{compareList[alg]: <10}')


main()
