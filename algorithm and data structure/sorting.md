a short summary of RealPython blog:
- https://realpython.com/sorting-algorithms-python/#the-importance-of-sorting-algorithms-in-python
## The Importance of Sorting Algorithms

- Searching: Searching for an item on a list works much faster if the list is sorted.

- Selection: Selecting items from a list based on their relationship to the rest of the items is easier with sorted data. For example, finding the kth-largest or smallest value, or finding the median value of the list, is much easier when the values are in ascending or descending order.

- Duplicates: Finding duplicate values on a list can be done very quickly when the list is sorted.

- Distribution: Analyzing the frequency distribution of items on a list is very fast if the list is sorted. For example, finding the element that appears most or least often is relatively straightforward with a sorted list.

**python Built-in**

```python
>>> array = [8, 2, 6, 4, 5]
>>> sorted(array)
[2, 4, 5, 6, 8]
```

## Timing

- runtime (timeit)
- runtime complexity  (Big O)

```python
from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
```

code usage:

```python
ARRAY_LENGTH = 10000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="sorted", array=array)
```
```bash
$ python sorting.py
Algorithm: sorted. Minimum execution time: 0.010945824000000007
```
With Big O, you express complexity regarding how quickly your algorithm’s runtime grows relative to the input size, especially as the input grows arbitrarily large.



## Big O Complexity Table

| **Big O**    | **Complexity**    | **Description**                                                                                                                                     |
|---------------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **O(1)**      | constant          | The runtime is constant, independent of input size. Example: Accessing an element in a hash table.                                                  |
| **O(n)**      | linear            | The runtime grows linearly with input size. Example: Iterating through a list to check a condition on each element.                                |
| **O(n²)**     | quadratic         | The runtime is proportional to the square of the input size. Example: Naive duplicate detection by comparing each pair of elements in a list.      |
| **O(2ⁿ)**     | exponential       | The runtime doubles with each additional input. Example: Solving the three-coloring problem using brute force.                                     |
| **O(log n)**  | logarithmic       | The runtime increases linearly while input size grows exponentially. Example: Binary search in a sorted list.                                      |



## Bubble Sort Algorithm

```python
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array
```
<img src="https://github.com/user-attachments/assets/c35269b5-b0ca-46ec-9ac0-4783540c94c8" alt="image" width="300"/>

the comparisons that are done in the bubble sort
$(n - 1) + (n - 2) + (n - 3) + … + 2 + 1 = n(n-1)/2$
or 
$\frac{n^2}{2} -\frac{n}{2}$

it's about the growth wrt to the input size, so we would omit the 2s, and we would have $n^2 - n$, and because $n^2$ is bigger we would go with it.

# The Insertion Sort Algorithm


```python
def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Example usage
array = [8, 4, 6, 1]
sorted_array = insertion_sort(array)
print("Sorted Array:", sorted_array)
```
- best case "O(n)" : for sorted array

- worst case: $O(n^2)$

![Insertion-sort-example](https://github.com/user-attachments/assets/07295492-6ba3-4fd8-8445-4fd25bc3e6fa)
[wikipedia]

![image](https://github.com/user-attachments/assets/1c630226-a870-44d8-80d5-0585c21c3bf0)
[realpython]

- time complexity : $O(n^2)$

- worst case: reversed array $O(n^2)$
- best case: sorted $O(n)$

## Merge Sort Algorithm
divide-and-conquer approach
![image](https://github.com/user-attachments/assets/c9babbc4-6dfb-44d7-b916-b7bcdffa040a)

```python
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


sorted_array = merge_sort([1, 2, 3, 4, 5, 6, 76, 345, 0, 3, 45, 4, 3, 2])

print(sorted_array)
```
