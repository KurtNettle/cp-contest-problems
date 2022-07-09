# [B. Students Score](https://codeto.win/contest/43/problem/B)

<p>A student has to obtain at least <strong>45 </strong>marks to pass a course. You are given a students scores of Mid exam, Final exam and Class assessment. Can you tell me if the student has passed the course or not ?</p>

## Input
 
<p>You are given three integers, <strong>M</strong>, <strong>F </strong>and <strong>C</strong>, where <strong>M</strong> is the score of Mid exam, <strong>F</strong> is the score of Final exam and <strong>C</strong> is the score at Class assessment. (<strong>0<span style="font-size: 16.5px;">≤M</span><span style="font-size: 16.5px;">≤30</span></strong>), (<strong>0<span style="font-size: 16.5px;">≤F</span><span style="font-size: 16.5px;">≤40</span></strong>), (<strong>0<span style="font-size: 16.5px;">≤C</span><span style="font-size: 16.5px;">≤30</span></strong>)</p>

## Output
 
<p>If the student has passed the exam, print "<strong>Passed</strong>", otherwise print "<strong>Not Passed</strong>", without the quotes.</p>

## Samples

### Input

```
30 40 30
```

### Output

```
Passed

```
### Input

```
8 10 20
```

### Output

```
Not Passed

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
  int a, b, c;
  cin >> a >> b >> c;
  ((a + b + c) >= 45) ? (cout << "Passed\n") : (cout << "Not Passed\n");

}

int main() {
  
  solve();
  return 0;
}
```