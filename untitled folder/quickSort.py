
def quickSort(A):
    """
    """

    less = []
    greater = []
    equal = []

    if len(A) > 1:
        pivot = int((len(A) - 1)/2)
        for item in A:

            if item < A[pivot]:
                less += [item]
            elif item > A[pivot]:
                greater += [item]
            else:
                equal += [item]
        less = quickSort(less)
        greater = quickSort(greater)

        return less + equal + greater
    else:
        return A


A = [1, 2, 5, 7, 3, 55, 7, 8, 0, 9]

print quickSort(A)
