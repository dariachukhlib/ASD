#Zadanie 3
def theLargestElement(vector):
    if len(vector) == 0:
        return "Empty array"

    if len(vector) == 1:
        return vector[0]
    middle = len(vector) // 2
    left = vector[:middle]
    right = vector[middle:]

    maxL = theLargestElement(left)
    maxR = theLargestElement(right)

    return max(maxL, maxR)


vector = [70, 92, 91, 23, 93, 55, 93]
max = theLargestElement(vector)
print("Największy element wektora:", max)


#Zadanie 4
def sum(array):
    if len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]

    sumL = sum(left)
    sumR = sum(right)

    return sumL + sumR

array = [5, 7, 10, 13, 4, 10, 11]
suma = sum(array)
print("Suma elementów w tablicy:", suma)
