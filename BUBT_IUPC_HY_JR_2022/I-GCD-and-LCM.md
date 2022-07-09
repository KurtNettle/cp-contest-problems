# [I. GCD and LCM](https://codeto.win/contest/43/problem/I)


<p class="MsoNormal" style="margin-bottom: 6pt; line-height: normal;"><span style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; --darkreader-inline-bgimage: initial;" data-darkreader-inline-bgimage="">You’re now a senior programmer of BUBT. If we told you to find out
the GCD and LCM of two numbers, you will smile and can easily find them. We are
giving you the same task but in different constraints. <o:p></o:p></span></p>

<p class="MsoNormal" style="margin-bottom: 6pt; line-height: normal;"><span style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; --darkreader-inline-bgimage: initial;" data-darkreader-inline-bgimage="">Given two numbers a and b in range <strong>[1
, 10<sup>700000</sup>]</strong> and expecting that you can also find the<strong>&nbsp;GCD</strong>&nbsp;and <strong>LCM</strong>&nbsp;of
these numbers.<o:p></o:p></span></p>

<p class="MsoNormal" style="margin-bottom: 6pt; line-height: normal;"><span style="background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; --darkreader-inline-bgimage: initial;" data-darkreader-inline-bgimage="">As the number a and b are too big
which can not be fit in 64-bit integer so we are giving you the <strong>prime factorizations</strong>
of these numbers. Also, the <strong>GCD</strong> and <strong>LCM</strong> are big so print the<strong> output modulo 10<sup>9</sup>
+ 7.&nbsp;</strong><font style="--darkreader-inline-color: #e8e6e3;" data-darkreader-inline-color="" color="#000000"><span style="font-size: 12pt; background-color: white; --darkreader-inline-bgcolor: #181a1b;" data-darkreader-inline-bgcolor=""><o:p></o:p></span></font></span></p>

## Input
 
<p class="MsoNormal" style="margin-bottom: 0in;">First line starts with an integer <strong>N</strong>: Number of prime factors of<strong> a.</strong><br></p>

<p class="MsoNormal" style="margin-bottom: 0in;"><span style="line-height: 107%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; --darkreader-inline-bgimage: initial;" data-darkreader-inline-bgimage="">Second line has <strong>N</strong>
integers <strong>A<sub>1</sub>, A<sub>2</sub>, A<sub>3</sub>,…,A<sub>N</sub></strong>:<strong> </strong>Prime factors of<strong> a.</strong><o:p></o:p></span></p>

<p class="MsoNormal" style="margin-bottom: 0in;"><span style="line-height: 107%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; --darkreader-inline-bgimage: initial;" data-darkreader-inline-bgimage="">Next input integer
is <strong>M</strong>:<strong> </strong>Number of prime factors of <strong>b.</strong><o:p></o:p></span></p>

<p class="MsoNormal" style="margin-bottom: 0in;"><span style="line-height: 107%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; --darkreader-inline-bgimage: initial;" data-darkreader-inline-bgimage="">Finally, <strong>M</strong>
integers <strong>B<sub>1</sub>,B<sub>2</sub>,B<sub>3</sub>,…,B<sub>M</sub></strong>: Prime factors of <strong>b.</strong><o:p></o:p></span></p>

<span style="line-height: 107%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; --darkreader-inline-bgimage: initial;" data-darkreader-inline-bgimage=""></span>

<p class="MsoNormal" style="margin-bottom: 0in;"><span style="line-height: 107%; background-image: initial; background-position: initial; background-size: initial; background-repeat: initial; background-attachment: initial; background-origin: initial; background-clip: initial; --darkreader-inline-bgimage: initial;" data-darkreader-inline-bgimage=""><strong>Note:</strong> It is guaranteed
that the given array A and B contains only prime numbers. Also input integer can be in arbitrary order.<o:p></o:p></span></p>

## Constraints:

<p>1&nbsp;</span></strong>≤<strong><span>&nbsp;N , M&nbsp;</span></strong>≤<strong><span>&nbsp;10<sup>5&nbsp;</sup>&nbsp;</span></strong></p>
<p><span><strong>1&nbsp;</strong></span>≤&nbsp;<strong>Ai, Bi&nbsp;</strong>≤&nbsp;<strong>10<sup>7</sup></strong></p>

## Output
 
<p class="MsoNormal" style="line-height:105%"><span style="line-height: 105%;">For each test case print<strong> two space separated integers </strong>indicating <strong>GCD(a,b)
</strong>and <strong>LCM(a,b). </strong>Both integers should be<strong> modulo 10<sup>9</sup> + 7.</strong> See the sample I/O for
exact formatting.</span><span style="line-height: 105%;"><o:p></o:p></span></p><p><strong>Explanation: </strong></p><p class="MsoNormal"><o:p></o:p></p><p class="MsoNormal">1st Case: gcd(12, 8) = 4 and lcm(12,8) = 24<o:p></o:p></p><p class="MsoNormal">2nd Case: gcd(175,8085) = 35 and lcm(175,8085) = 40425<o:p></o:p></p>


## Samples

### Input

```
3
2 2 3
3
2 2 2
```

### Output

```
4 24

```
### Input

```
3
3 5 7
5
5 5 7 7 11
```

### Output

```
35 40425

```
## My Approach
```c++

```
