#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
  int maxAscendingSum(vector<int> &nums) {
    // [10,20,30,5,10,50]
    int sum = 0;
    int previous_number = 0;
    int previous_sum = 0;

    for (auto number : nums) {
      if (number < previous_number || number == previous_number) {
        if (previous_sum < sum) {
          previous_sum = sum;
        }

        sum = number;
        previous_number = number;
        continue;
      }

      sum += number;
      previous_number = number;

      /*std::cout << number << std::endl;*/
    }

    std::cout << sum << " " << previous_sum << std::endl;

    return ((sum > previous_sum) ? sum : previous_sum);
  }
};

int main() {
  Solution as;

  vector<int> input1{10, 20, 30, 5, 10, 50};
  std::cout << "Result is: " << as.maxAscendingSum(input1) << std::endl;

  vector<int> input2{10, 20, 30, 40, 50};
  std::cout << "Result is: " << as.maxAscendingSum(input2) << std::endl;

  vector<int> input3{12, 17, 15, 13, 10, 11, 12};
  std::cout << "Result is: " << as.maxAscendingSum(input3) << std::endl;

  vector<int> input4{3, 6, 10, 1, 8, 9, 9, 8, 9};
  std::cout << "Result is: " << as.maxAscendingSum(input4) << std::endl;
}
