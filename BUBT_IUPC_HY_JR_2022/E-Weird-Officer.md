# [E. Weird Officer](https://codeto.win/contest/43/problem/E)

<div id="statement">
<p class="MsoNormal" style="margin: 12pt 0in 6pt;"><span lang="EN" style="line-height: 115%;">Our Abu Quwsar Ohi Sir is
departing our country after receiving a scholarship for higher education. At
the airport, an immigration official questioned Abu Quwsar Ohi sir is, <o:p></o:p></span></p>
<p class="MsoNormal" style="margin: 12pt 0in 6pt;"><span lang="EN" style="line-height: 115%;">You’re given a positive
integer <strong>M</strong>, find the largest integer <strong>X</strong> such that <strong>2<sup>x</sup> </strong></span><span lang="EN" style="line-height: 115%;"><strong>≤ M</strong></span><span lang="EN" style="line-height: 115%;">. He challenged you to solve the problem.</span></p>
</div>

## Input
 
<p class="MsoNormal" style="margin-top:12.0pt;text-align:justify">You are given an integer <strong>M</strong>. Here, <strong>M </strong>is an integer satisfying <strong>1 ≤ M ≤ 10<sup>18</sup></strong></p>

## Output
 
<p class="MsoNormal" style="margin-top:12.0pt;margin-right:0in;margin-bottom:
12.0pt;margin-left:0in;line-height:105%"><span lang="EN" style="line-height: 105%;">Print the answer to the problem.</span></p>

## Samples

### Input

```
6
```

### Output

```
2

```
### Input

```
1
```

### Output

```
0

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
  unsigned long long int x = 0, i = 0;
  cin >> x;
  for (i = 0; (powl(2, i) <= x); ++i) {
  }
  cout << i - 1 << endl;
  // code here
}

int main() {
  solve();
  return 0;
}
```