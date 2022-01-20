#include <iostream>
#include <vector>
#include <algorithm>

int MaxPairwiseProductNaive(const std::vector<int>& numbers) {
    int max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,  numbers[first] * numbers[second]);
        }
    }

    return max_product;
}


int MaxPairwiseProduct(const std::vector<int>& numbers) {
    int index1;
    int index2;
    int max_product;
    int n = numbers.size();

    if (numbers[1] > numbers[0]) {
        index1 = 1;
        index2 = 0;
    } else {
        index1 = 0;
        index2 = 1;
    }

    for (int i = 2; i < n; ++i) {
        if (numbers[index1] <= numbers[i]) {
            index2 = index1;
            index1 = i;
        } else if (numbers[index2] <= numbers[i]) {
            index2 = i;
        }
    }

    max_product = numbers[index1] * numbers[index2];
    return max_product;
}

void StressTest(int n, int m) {
    while(true) {
        int length_of_numbers = rand() % n + 2;
        std::cout << "length_of_numbers: " << length_of_numbers << "\n";
        std::vector<int> numbers(length_of_numbers);
        for (int i = 0; i < length_of_numbers; i++) {
            numbers[i] = rand() % m + 1;
            std::cout << numbers[i] << " ";
        }
        int result1 = MaxPairwiseProductNaive(numbers);
        int result2 = MaxPairwiseProduct(numbers);

        if (result1 == result2) {
            std::cout << "OK" << "\n";
        } else {
            std::cout << "ERROR" << "\n";
            break;
        }
    }
}

int main() {
    StressTest(30, 1000);
    return 0;
}
