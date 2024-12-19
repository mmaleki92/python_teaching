# Hands-on Problems for Threading and Multiprocessing

## Threading Problems

1. **Simple Counter**  
   Create a program that starts 5 threads, each of which increments a global counter 1000 times. Use a `threading.Lock` to ensure thread safety.

2. **Downloading Data**  
   Simulate downloading data by creating 3 threads that sleep for random durations and print when they start and finish downloading.

3. **Prime Number Check**  
   Divide a range of numbers (e.g., 1 to 1000) across 4 threads to check if the numbers are prime. Print the prime numbers found by each thread.

4. **File Search**  
   Create a program where multiple threads search for a specific word in different text files. Return the filenames that contain the word.

5. **Producer-Consumer**  
   Implement a producer-consumer problem using a `queue.Queue`. The producer adds numbers to the queue, and the consumer removes them and prints them.

6. **Matrix Row Sum**  
   Calculate the sum of each row in a matrix using a thread for each row. Combine the results and print the total sum.

7. **Thread-safe Dictionary**  
   Use a `threading.Lock` to safely update a shared dictionary from multiple threads. Each thread should add a unique key-value pair.

8. **Sorting with Threads**  
   Split a list into parts, sort each part using a separate thread, and merge the results into a sorted list.

9. **Fibonacci Numbers**  
   Calculate the first 20 Fibonacci numbers using threads. Assign one thread to calculate each Fibonacci number.

10. **Threaded Timer**  
    Create a multi-threaded program that has 3 threads, each printing a message at different intervals (e.g., every 1, 2, and 3 seconds).

---

## Multiprocessing Problems

1. **Parallel Square Calculation**  
   Use multiprocessing to calculate the squares of a list of numbers. Split the list into equal parts for multiple processes.

2. **Shared Counter**  
   Create a program that uses multiple processes to increment a shared counter using `multiprocessing.Value` or `multiprocessing.Manager`.

3. **File Copying**  
   Use multiple processes to copy a list of files from one directory to another.

4. **Image Resizing**  
   Use multiprocessing to resize a set of images in parallel. Use the Pillow library for image resizing.

5. **Sorting Large List**  
   Divide a large list into chunks, sort each chunk using separate processes, and merge the results in the main process.

6. **Matrix Multiplication**  
   Use multiple processes to perform matrix multiplication. Assign each process a part of the result matrix to calculate.

7. **Log Analysis**  
   Process a large log file using multiprocessing to count the occurrence of a specific word in different chunks of the file.

8. **Parallel Web Scraping**  
   Use multiple processes to scrape data from a list of URLs. Each process should handle a subset of URLs.

9. **Word Count**  
   Divide a text document into parts and use multiprocessing to count the frequency of each word in parallel. Combine the results in the main process.

10. **Monte Carlo Simulation**  
    Estimate the value of π using the Monte Carlo method, dividing the total number of points among multiple processes.
