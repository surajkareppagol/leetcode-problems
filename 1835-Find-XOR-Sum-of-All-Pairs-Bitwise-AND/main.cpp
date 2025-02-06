#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
  int getXORSum(vector<int> &arr1, vector<int> &arr2) {
    /* ATTEMPTED */

    /*int XOR_sum = 0;*/
    /*vector<int> AND_values{};*/
    /**/
    /*for (int i = 0; i < std::size(arr1); i++) {*/
    /*  for (int j = 0; j < std::size(arr2); j++) {*/
    /*    AND_values.push_back(arr1[i] & arr2[j]);*/
    /*  }*/
    /*}*/
    /**/
    /*for (int i = 0; i < std::size(AND_values); i++) {*/
    /*  XOR_sum ^= AND_values[i];*/
    /*}*/
    /**/
    /*return XOR_sum;*/
    int XOR_arr1{};
    for (int i = 0; i < std::size(arr1); i++) {
      XOR_arr1 ^= arr1[i];
    }

    int XOR_arr2{};
    for (int i = 0; i < std::size(arr2); i++) {
      XOR_arr2 ^= arr2[i];
    }

    return XOR_arr1 & XOR_arr2;
  }
};

int main() {
  vector<int> arr1{1, 2, 3};
  vector<int> arr2{6, 5};

  Solution solution{};
  int XOR_sum = solution.getXORSum(arr1, arr2);

  std::cout << XOR_sum << std::endl;
  return 0;
}
