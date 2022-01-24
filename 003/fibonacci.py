# Uses python3
import random


def calc_fib_recursive(n):
    if n <= 1:
        return n

    return calc_fib_recursive(n - 1) + calc_fib_recursive(n - 2)


def calc_fib_table(n):
    if n <= 1:
        return n

    numbers = [None] * n
    for i in range(n):
        if i <= 1:
            numbers[i] = 1
        else:
            numbers[i] = numbers[i-1] + numbers[i-2]

    return numbers[i]


def stress_test(max_n=45):
    while True:
        n = random.randint(1, max_n)
        print(str(n))
        result1 = calc_fib_recursive(n)
        result2 = calc_fib_table(n)
        print(f"result1: {result1}, result2: {result2}")
        if result1 == result2:
            print("OK")
        else:
            print("ERROR")
            break


if __name__ == "__main__":
    # n = int(input())
    # print(calc_fib_recursive(n))
    # print(calc_fib_table(n))
    stress_test()
