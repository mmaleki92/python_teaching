# Solutions for Threading and Multiprocessing Problems

## Threading Solutions

1. **Simple Counter**

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print("Final Counter:", counter)
```

2. **Downloading Data**


```python
import threading
import time
import random

def download_data(thread_id):
    print(f"Thread {thread_id} started downloading.")
    time.sleep(random.randint(1, 5))
    print(f"Thread {thread_id} finished downloading.")

threads = [threading.Thread(target=download_data, args=(i,)) for i in range(3)]

for t in threads:
    t.start()
for t in threads:
    t.join()

```
3. Prime Number Check

```python
import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end):
    for n in range(start, end):
        if is_prime(n):
            print(f"Prime found: {n}")

threads = [threading.Thread(target=check_primes, args=(i, i+250)) for i in range(1, 1000, 250)]

for t in threads:
    t.start()

for t in threads:
    t.join()
```

4. File Search

```python
import threading

def search_file(filename, word):
    with open(filename, 'r') as f:
        if word in f.read():
            print(f"Word found in {filename}")

files = ["file1.txt", "file2.txt", "file3.txt"]
threads = [threading.Thread(target=search_file, args=(file, "target_word")) for file in files]
for t in threads: t.start()
for t in threads: t.join()

```

5. Producer-Consumer

```python
import threading
import queue
import random
import time

q = queue.Queue()

def producer():
    for i in range(10):
        num = random.randint(1, 100)
        q.put(num)
        print(f"Produced: {num}")
        time.sleep(1)

def consumer():
    while not q.empty() or threading.active_count() > 2:
        if not q.empty():
            num = q.get()
            print(f"Consumed: {num}")
        time.sleep(0.5)

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()

```

6. Matrix Row Sum

```python
import threading

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
results = []
lock = threading.Lock()

def row_sum(row):
    total = sum(row)
    with lock:
        results.append(total)

threads = [threading.Thread(target=row_sum, args=(row,)) for row in matrix]
for t in threads: t.start()
for t in threads: t.join()

print("Total Sum:", sum(results))

```

7. Thread-safe Dictionary

```python
import threading

shared_dict = {}
lock = threading.Lock()

def add_to_dict(key, value):
    with lock:
        shared_dict[key] = value

threads = [threading.Thread(target=add_to_dict, args=(i, i**2)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print("Dictionary:", shared_dict)

```

8. Sorting with Threads

```python
import threading

def sort_sublist(sublist):
    sublist.sort()

lst = [4, 1, 7, 3, 9, 2, 8, 5, 6]
mid = len(lst) // 2
left, right = lst[:mid], lst[mid:]

t1 = threading.Thread(target=sort_sublist, args=(left,))
t2 = threading.Thread(target=sort_sublist, args=(right,))
t1.start(); t2.start()
t1.join(); t2.join()

lst = sorted(left + right)
print("Sorted List:", lst)

```

9. Fibonacci Numbers

```python
import threading

fib_results = {}
lock = threading.Lock()

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def calculate_fib(n):
    result = fibonacci(n)
    with lock:
        fib_results[n] = result

threads = [threading.Thread(target=calculate_fib, args=(i,)) for i in range(20)]
for t in threads: t.start()
for t in threads: t.join()

print("Fibonacci Numbers:", fib_results)

```

10. Threaded Timer

```python
import threading
import time

def print_message(interval, message):
    while True:
        time.sleep(interval)
        print(message)

threads = [
    threading.Thread(target=print_message, args=(1, "Every second")),
    threading.Thread(target=print_message, args=(2, "Every 2 seconds")),
    threading.Thread(target=print_message, args=(3, "Every 3 seconds"))
]
for t in threads: t.start()

```


# Solutions for Multiprocessing Problems

1. **Parallel Square Calculation**

```python
from multiprocessing import Pool

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
with Pool(4) as pool:
    results = pool.map(square, numbers)

print("Squares:", results)
```

2. Shared Counter

```python
from multiprocessing import Process, Value, Lock

def increment(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1

counter = Value('i', 0)
lock = Lock()
processes = [Process(target=increment, args=(counter, lock)) for _ in range(5)]

for p in processes: p.start()
for p in processes: p.join()

print("Final Counter:", counter.value)

```

3. File Copying

```python

import shutil
from multiprocessing import Process

def copy_file(src, dest):
    shutil.copy(src, dest)

files = [("source1.txt", "dest1.txt"), ("source2.txt", "dest2.txt"), ("source3.txt", "dest3.txt")]
processes = [Process(target=copy_file, args=(src, dest)) for src, dest in files]

for p in processes: p.start()
for p in processes: p.join()

print("Files copied.")

```

4. Image Resizing

```python

from multiprocessing import Process
from PIL import Image

def resize_image(image_path, output_path, size):
    img = Image.open(image_path)
    img = img.resize(size)
    img.save(output_path)

tasks = [
    ("image1.jpg", "resized1.jpg", (100, 100)),
    ("image2.jpg", "resized2.jpg", (100, 100)),
    ("image3.jpg", "resized3.jpg", (100, 100))
]
processes = [Process(target=resize_image, args=task) for task in tasks]

for p in processes: p.start()
for p in processes: p.join()

print("Images resized.")
```

5. Sorting Large List

```python

from multiprocessing import Pool

def sort_chunk(chunk):
    return sorted(chunk)

data = [8, 3, 7, 1, 9, 2, 6, 5, 4]
chunk_size = len(data) // 2
chunks = [data[:chunk_size], data[chunk_size:]]

with Pool(2) as pool:
    sorted_chunks = pool.map(sort_chunk, chunks)

sorted_data = sorted(sorted_chunks[0] + sorted_chunks[1])
print("Sorted List:", sorted_data)

```

6. Matrix Multiplication

```python
from multiprocessing import Process

def calculate_element(A, B, result, row, col):
    result[row][col] = sum(A[row][k] * B[k][col] for k in range(len(A[0])))

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = [[0] * len(B[0]) for _ in range(len(A))]

processes = []
for i in range(len(A)):
    for j in range(len(B[0])):
        p = Process(target=calculate_element, args=(A, B, result, i, j))
        processes.append(p)
        p.start()

for p in processes: p.join()
print("Resultant Matrix:", result)
```

7. Log Analysis

```python

from multiprocessing import Pool

def count_word_in_chunk(chunk, word):
    return chunk.count(word)

with open("logfile.txt", "r") as f:
    data = f.read()

chunks = [data[i:i+100] for i in range(0, len(data), 100)]
with Pool(4) as pool:
    results = pool.starmap(count_word_in_chunk, [(chunk, "error") for chunk in chunks])

print("Total occurrences of 'error':", sum(results))


```

8. Parallel Web Scraping

```python
import requests
from multiprocessing import Pool

def fetch_url(url):
    response = requests.get(url)
    return url, len(response.content)

urls = ["http://example.com", "http://example.org", "http://example.net"]
with Pool(3) as pool:
    results = pool.map(fetch_url, urls)

for url, content_length in results:
    print(f"{url}: {content_length} bytes")
```

9. Word Count

```python

from multiprocessing import Pool

def count_words(chunk):
    words = chunk.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

with open("textfile.txt", "r") as f:
    data = f.read()

chunks = [data[i:i+200] for i in range(0, len(data), 200)]
with Pool(4) as pool:
    results = pool.map(count_words, chunks)

final_count = {}
for partial_count in results:
    for word, count in partial_count.items():
        final_count[word] = final_count.get(word, 0) + count

print("Word Counts:", final_count)

```

10. Monte Carlo Simulation

```python

from multiprocessing import Pool
import random

def monte_carlo_pi(samples):
    inside_circle = 0
    for _ in range(samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return inside_circle

total_samples = 1000000
num_processes = 4
samples_per_process = total_samples // num_processes

with Pool(num_processes) as pool:
    results = pool.map(monte_carlo_pi, [samples_per_process] * num_processes)

pi_estimate = (4 * sum(results)) / total_samples
print("Estimated π:", pi_estimate)

```
