import random


def max_pairwise_product_naive(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])
    return max_product


def max_pairwise_product(numbers):
    """
    Returns maximal pairwise product.

    Index1 stores index of the greatest number
    Index2 stores index of the second greatest number

    :param numbers: list of numbers
    :return: maximal product
    """
    n = len(numbers)

    index1 = 1 if numbers[1] > numbers[0] else 0
    index2 = 0 if index1 == 1 else 1

    for i in range(2, n):
        if numbers[index1] <= numbers[i]:
            index2 = index1
            index1 = i
        elif numbers[index2] <= numbers[i]:
            index2 = i

    max_product = numbers[index1] * numbers[index2]
    return max_product


def stress_test(n, m):
    while True:
        length_of_numbers = random.randint(2, n)
        print(str(length_of_numbers))
        numbers = [random.randint(1, m) for _ in range(length_of_numbers)]
        print(str(numbers))
        result1 = max_pairwise_product_naive(numbers)
        result2 = max_pairwise_product(numbers)
        if result1 == result2:
            print("OK")
        else:
            print("ERROR")
            break


def main():
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))


if __name__ == '__main__':
    # main()
    stress_test(30, 100000000)
