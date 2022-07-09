# [F. String Task](https://codeto.win/contest/43/problem/F)

<div id="statement">
<span id="docs-internal-guid-d7994d43-7fff-0039-d0bd-4fb06d0ead3f"></span><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">Dipu sir gives a string to Maruf to identify whether it is palindrome or not. He gives condition-</span></p><span id="docs-internal-guid-0dd2cc25-7fff-7722-2900-4c427b1e46e7"></span><p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">For each position in the string, Maruf has to change the letter on this position either to the previous letter in alphabetic order or to the next one. But 'a' has no previous letter and 'z' has no next letter. Letter in </span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><strong>every position</strong></span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"> must be changed </span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><strong>exactly once</strong></span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">.</span></p>
</div>

## Input
 
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">First line contains the number of test</span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"> cases</span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"> </span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><strong>T</strong></span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">. The first line of the pair has a single integer <strong>N</strong> which is the length of the string, then take the string <strong>S</strong>.</span></p>

## Output
 
<p dir="ltr" style="line-height:1.38;margin-top:0pt;margin-bottom:0pt;"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">Print "<strong>Yeahh</strong><strong>!</strong>" if it's possible to make the string a palindrome by applying the changes as mentioned above to every position. Print "<strong>opps!</strong>" otherwise.</span></p>

## Samples

### Input

```
4
6
abccba
2
af
4
adfa
8
abaazaba
```

### Output

```
Yeahh!
opps!
Yeahh!
opps!

```

## Explanation
You will get a better understanding by reading the problem description from [here](https://codeforces.com/problemset/problem/1027/A) since it's a direct rip off with shortened description.

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
  int n;
  cin >> n;
  string s;
  cin >> s;

  for (int i = 0; i < (n / 2); ++i) {
    int x = abs(s[i] - s[(n - 1) - i]);
    if (x != 0 and x != 2) {
      cout << "opps!\n";
      return;
    }
  }
  cout << "Yeahh!\n";
}

int main() {
  int tests;
  cin >> tests;
  while (tests--) solve();

  return 0;
}
```
