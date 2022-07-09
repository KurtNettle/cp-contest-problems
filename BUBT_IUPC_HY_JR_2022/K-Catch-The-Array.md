# [K. Catch The Array](https://codeto.win/contest/43/problem/K)

<div id="statement">
<p class="MsoNormal" style="margin-top:3.45pt;margin-right:54.05pt;margin-bottom:
0in;margin-left:0in;margin-bottom:.0001pt;line-height:113%;mso-pagination:none;
text-autospace:none"><span style="line-height: 113%;">You are
given a sequence of positive integers of length </span><span style="line-height: 113%;"><strong>N</strong></span><span style="line-height: 113%;">, </span><span style="line-height: 113%;"><strong>A</strong> = A<sub>1</sub>, A<sub>2</sub>, …, A<sub>N</sub></span><span style="line-height: 113%;">, and
an integer </span><span style="line-height: 113%;"><strong>K</strong></span><span style="line-height: 113%;">.</span><span style="line-height: 113%;"> </span><span style="line-height: 113%;">How many
contiguous subsequences of </span><span style="line-height: 113%;">A </span><span style="line-height: 113%;">satisfy the following condition- </span></p><ul><li>The sum of the elements in the contiguous subsequence is at least <span style="line-height: 113%;"><strong>K.</strong></span></li></ul>
<p class="MsoNormal" style="margin-top:3.45pt;margin-right:54.05pt;margin-bottom:
0in;margin-left:0in;margin-bottom:.0001pt;line-height:113%;mso-pagination:none;
text-autospace:none"><span style="line-height: 113%;">We consider
two contiguous subsequences different, if they start from different positions in
<strong>A</strong>, even if they are the same in content.<o:p></o:p></span></p>
<p class="MsoNormal" style="margin-top:3.45pt;margin-right:54.05pt;margin-bottom:
0in;margin-left:0in;margin-bottom:.0001pt;line-height:113%;mso-pagination:none;
text-autospace:none"><span style="line-height: 113%;"><strong>Note that,</strong> the answer
may not fit into a </span><span style="line-height: 113%;">32</span><span style="line-height: 113%;">-bit integer
type.<strong><font face="Tahoma, sans-serif"><span style="font-size: 12pt;"><o:p></o:p></span></font></strong></span></p>
</div>

## Input
 
<p class="MsoNormal" style="margin: 12pt 0in 6pt;"><span lang="EN" style="line-height: 115%;">The
first line contains two integers N (<strong>1≤N≤10<sup>5</sup></strong>) length of the array and</span> an integer K (<strong>1≤K≤10<sup>10</sup></strong>).</p>

## Output
 
<p class="MsoNormal" style="margin-top:12.0pt;margin-right:0in;margin-bottom:
12.0pt;margin-left:0in;line-height:105%"><span lang="EN" style="line-height: 105%;">Print the <strong>number of contiguous
subsequences</strong> of A that satisfy the condition.<font face="Tahoma, sans-serif"><span style="font-size: 12pt;"><o:p></o:p></span></font></span></p>

## Samples

### Input

```
4 10
6 1 2 7
```

### Output

```
2

```
### Input

```
3 5
3 3 3
```

### Output

```
3

```
### Input

```
10 53462
103 35322 232 342 21099 90000 18843 9010 35221 19352
```

### Output

```
36

```
## My Approach
```c++

```
