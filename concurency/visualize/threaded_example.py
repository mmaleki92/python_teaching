
# https://opensource.com/article/21/3/python-viztracer
import random
from threading import Thread

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_prime_arr(arr):
    return [is_prime(elem) for elem in arr]


if __name__ == "__main__":
    num_arr = [random.randint(100, 10000) for i in range(2000)]
    thread1 = Thread(target=get_prime_arr, args=(num_arr,))
    thread2 = Thread(target=get_prime_arr, args=(num_arr,))
    thread3 = Thread(target=get_prime_arr, args=(num_arr,))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()