# [C. Shooting tiles](https://codeto.win/contest/43/problem/C)

<div id="statement">
<p>There are <strong>N</strong> tiles that you have to shoot. The tiles are numbered <strong>sequentially</strong>, that means,</p><p>if the 1<sup>st</sup> tile has the number 4,</p><p>the 2<sup>nd</sup> tile will have 5 and </p><p>the 3<sup>rd</sup> tile will have 6 and so on. </p><p>You are told the first tile has the number <strong>A</strong>.</p><p>If you shoot a tile, the number written on the tile is added to your point. If you have <strong>0 points</strong> before starting, what will be your total point after shooting <strong>N</strong> tiles ?</p><p>You can shoot a tile <strong>only once</strong>.</p>
</div>

## Input
 
<p>First line gives an integer <strong>T</strong>, denoting the number of test cases. (<strong>1<span style="font-size: 16.5px;">≤T</span><span style="font-size: 16.5px;">≤1000</span></strong>)</p>

## Output
 
<p>For each test case, print the <strong>total point</strong> you get after shooting the <strong>N</strong> tiles.</p>

## Samples

### Input

```
3
4 2
5 2
7 3
```

### Output

```
14
20
42

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
  int n, a, s = 0;
  cin >> n >> a;
  for (int i = a, j = 0; j < n; ++i, ++j)
    s += i;
  cout << s << endl;
  // code here
}

int main() {

  int t;
  cin >> t;
  while (t--) {
    solve();
  }
  return 0;
}
```