# [D. Pair Pair](https://codeto.win/contest/43/problem/D)

One day, Mohsin Kabir Sir came to the class and gave you a task. He gave you an array A containing 2*N integers that may contain multiple equal values. Determine whether you can divide the array into exactly N pairs, so that the sum of the two elements of each pair is odd. Each element should only be in one pair.

## Input

The first line gives an integer T, denoting the number of test cases.

In the first line of each test case, you are given N.

Next line gives an array A containing 2*N space separated integers.

## Constrains:

1 ≤ T ≤ 100

1 ≤ Si ≤ 100

## Output

Print the test case number in this format "Test case T : ", where T is the number of test case. Then print "Yes" if it is possible, otherwise print "No".

## Samples

### Input
```
4
2
2  3  4  5
3
2  3  4  5  5  5
1
2  3
4
1  5  3  2  6  7  3  4
```

### Output
```
Test case 1: Yes
Test case 2: No
Test case 3: Yes
Test case 4: No

```

## My Solution

```c++
#include <math.h>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <numeric>

using namespace std;
using ll = long long int;

void solve(int tc) {
  int n, odd = 0, even = 0;
  cin >> n;
  
  for (int i = 0; i < (n * 2); ++i) {
    int x;
    cin >> x;
    (x & 1) ? (++odd) : (++even);
  }
  
  (odd == even) ? (printf("Test case %d: Yes\n", tc)) : (printf("Test case %d: No\n", tc));
}

int main() {
  
  int tests, tc = 1;
  cin >> tests;
  
  while (tests--) {
    solve(tc);
    ++tc;
  };

  return 0;
}
```