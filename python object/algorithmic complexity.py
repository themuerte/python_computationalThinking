import time
import sys

def factrorial(number):
    answer = 1

    while number > 1:
        answer *= number
        number -=1

    return answer

def factrorial_r(number):
    if number == 1:
        return 1
    
    return number * factrorial_r(number - 1)

if __name__ == "__main__":
    number = 1000

    #recurrence values ​​are total in a program, such that number < setrecursionlimit()
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(1500)

    start = time.time()
    factrorial(number)
    end = time.time()
    print(end - start) 

    start = time.time()
    factrorial_r(number)
    end = time.time()
    print(end - start)

