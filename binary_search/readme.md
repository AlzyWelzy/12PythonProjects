# Binary Search

This is a Python implementation of the binary search algorithm. The algorithm has a time complexity of `O(log n)`, making it faster than naive search which has a time complexity of `O(n)`.

## Getting Started

To use this implementation, import the `binary_search` function and the necessary dependencies.

```python
import json
import random
import time

from binary_search import binary_search, naive_search

with open('binary_search/data.json') as f:
    l = json.loads(f.read()).get("data")
```

The binary_search function takes in a sorted list and a target value, and returns the index at which the target value is found in the list. If the target value is not found in the list, the function returns -1.

```python
target = "whisper"
result = binary_search(l, target)
print(result) # 7
```

The implementation also includes a naive_search function for comparison, which has a time complexity of O(n).

```python
result = naive_search(l, target)
print(result) # 7
```

## Performance

To compare the performance of binary_search and naive_search, the implementation includes a simple benchmark that generates a sorted list of random integers and searches for each element in the list using both algorithms. The average search time for each algorithm is then calculated and printed.

```python
if __name__ == '__main__':
    length = 10000

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))

    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end-start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end-start)/length, "seconds")
```
