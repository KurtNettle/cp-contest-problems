# [A. Double it up](https://codeto.win/contest/43/problem/A)

<p>You have <strong>N</strong> oranges in a bucket. There is a button in the bucket that doubles up the number of oranges. How many oranges will there be if you push the button <strong>just once</strong>?</p>

## Input
 
<p>You will be given just an integer <strong>N(0 </strong>≤ <strong>N </strong>≤ <strong>500)</strong>.</p>

## Output
 
<p>Print the <strong>number of oranges</strong> in that bucket after you push the button once.</p>

## Samples

### Input

```
4
```

### Output

```
8

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
using ll = long long int;

void solve() {
  int x;
  cin >> x;
  cout << (x * 2) << "\n";
}

int main() {
  
  solve();
  return 0;
}
```
