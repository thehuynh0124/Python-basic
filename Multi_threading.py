import time
import threading

def square(numbers):
    print("Calculate square of numbers")
    for number in numbers:
        time.sleep(1)
        print("Square: ", number * number)

def cube(numbers):
    print("Calculate cube of numbers")
    for number in numbers:
        time.sleep(1)
        print("cube: ", number * number * number)

t =  time.time()
arr = [1, 3, 5, 7, 9]
thread1 = threading.Thread(target= square, args=(arr,))
thread2 = threading.Thread(target= cube, args=(arr,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

#square(arr)
#cube(arr)
print("done in ", time.time()- t)
