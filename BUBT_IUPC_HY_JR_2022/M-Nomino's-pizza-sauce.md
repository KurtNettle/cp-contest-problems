# [M. Nomino's pizza sauce](https://codeto.win/contest/43/problem/M)

<div id="statement">
<p>Nomino made a pizza of <strong>D</strong> diameter and cut it into <strong>N</strong> equal slices. He went to bring a bottle of tomato ketchup for the pizza. When he came back, he found that one of the slices was gone !! It must be ratatouille ! He uses <strong>W</strong> grams of ketchup per unit area of a pizza, he wants to know how much sauce he needs now to cover the left pizza.</p><p>So Nomino called you to calculate the <strong>amount of sauce</strong> he needs now.</p>
</div>

## Input
 
<p>The first line gives an integer <strong>T</strong>, denoting the number of test cases.</p><p>For each test case you are given three integers <strong>D</strong>, <strong>N</strong> and <strong>W</strong>, where <strong>D</strong> is the diameter of the pizza, <strong>N</strong> is the number of slices that were made initially, <strong>W</strong> is the amount of sauce domino uses per unit area of the pizza.</p>

## Constrains:
<p>1 ≤ <strong>T</strong> ≤ 10<sup>5</sup></p><p>1 ≤ <strong>D,N,W</strong> ≤ 10<sup>3</sup></p>


## Output
 
<p>For each test case, print the<strong> amount of sauce</strong> Nomino needs in grams. Print the amount <strong>rounded upto 6</strong> decimal points. </p>

## Samples

### Input

```
2
5 4 20
5 7 20
```

### Output

```
294.524311
336.599213

```
## My Approach
```c++
#include <math.h>
#include <string.h>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <numeric>

using namespace std;
using ll = long long;

void solve() {
  double d, n, w, full_pizza;
  cin >> d >> n >> w;
  full_pizza = M_PI * (pow((d / 2.0), 2));
  printf("%.6lf\n", (full_pizza * w) - ((full_pizza / n) * w));
  // code here
}

int main() {
  int tests;
  cin >> tests;
  while (tests--) solve();

  return 0;
}

```
