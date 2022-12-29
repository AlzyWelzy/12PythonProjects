import json
import random
import time

# Load the data from the data.json file
with open('binary_search/data.json') as f:
    l = json.loads(f.read()).get("data")

# Function to perform a naive search for a target value in a list


def naive_search(l, target):
    # Iterate through the list and return the index if the target is found
    for i in range(len(l)):
        if l[i] == target:
            return i
    # Return -1 if the target is not found
    return -1

# Function to perform a binary search for a target value in a sorted list


def binary_search(l, target, low=None, high=None):
    # Set the default low value to 0 if not provided
    if low is None:
        low = 0
    # Set the default high value to the length of the list - 1 if not provided
    if high is None:
        high = len(l)-1
    # Return -1 if the high value is less than the low value
    if high < low:
        return -1
    # Calculate the midpoint of the list
    midpoint = (low+high)//2
    # Return the midpoint if the target is found at the midpoint
    if l[midpoint] == target:
        return midpoint
    # Recursively search the left half of the list if the target is less than the value at the midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    # Recursively search the right half of the list if the target is greater than the value at the midpoint
    else:
        return binary_search(l, target, midpoint+1, high)


# Main function to compare the performance of the two search algorithms
if __name__ == '__main__':
    # Uncomment the following lines to test the search functions with a specific target value
    # target = "whisper"
    # print(naive_search(l, target))
    # print(binary_search(l, target))

    # Set the length of the list to search
    length = 10000

    # Generate a sorted list of random integers
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # Measure the time taken to perform a naive search for each element in the list
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end-start)/length, "seconds")

    # Measure the time taken to perform a binary search for each element in the list
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end-start)/length, "seconds")
