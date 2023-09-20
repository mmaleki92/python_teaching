from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    with Pool() as pool:
        result = pool.map(square, numbers)
    print(result) # Output: [1, 4, 9, 16, 25]