import random

def mode(numbers):

    if len(numbers) == 0:
        return None

    # Dictionary that track number:frequency
    dict = {}

    mode = 0
    mostFrequent = 0

    for element in numbers:
        # Set dictionary if number not already in, count is 0 but it'll become 1 after the set in dictionary
        if element not in dict:
            dict[element] = 0
        # The element just added appear one time or it already appeared in dict
        dict[element] += 1

        # I want to track at every step the mode and the relative frequency
        if dict[element] > mostFrequent:
            mostFrequent = dict[element]
            mode = element

    return mode


assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
assert mode([5, 6, 8, 0, 5, 3, 2, 1, 7, 5, 1, 7, 5]) == 5

random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):

    random.shuffle(testData)

    assert mode(testData) == 4
