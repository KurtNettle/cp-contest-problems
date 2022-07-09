# [L. World's Longest Marine Drive](https://codeto.win/contest/43/problem/L)

<div id="statement">
<span id="docs-internal-guid-405ce9d1-7fff-5b3f-215c-d694cf8a2c73"></span><p dir="ltr" style="line-height: 1.2; margin-top: 0pt; margin-bottom: 6pt;"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">Cox's Bazar–Teknaf Marine Drive is an 80-kilometer-long road from Cox's Bazar to Teknaf along the Bay of Bengal and it is the world's longest marine drive.</span></p><p dir="ltr" style="line-height: 1.2; margin-top: 0pt; margin-bottom: 6pt;"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">Mr x is planning for a solo trip to Cox bazar. He will stay <strong>N</strong> days and want to ride a bike as much as he can on each day. He has <strong>W</strong> TK for this purpose. Bike rental costs 100 TK per hour and an additional 50 Tk service charge without fuel. He has to refill fuel.1 liter of fuel costs 100 Tk and the bike can cover 50 km in one liter of fuel.</span>If the max speed of the bike is 50 km/h,  what is the maximum number of minimum kilometers he can ride each day?</p><p dir="ltr" style="line-height: 1.2; margin-top: 12pt; margin-bottom: 12pt;"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">Let’s say he wants to ride 75 km on the 1st day. He has to rent a bike for 2 hours and needs 2 liters of fuel. Total Cost will be 450Tk. 200 Tk rental fees and 200 Tk fuel fees and 50 Tk service fees. ‌</span></p><span id="docs-internal-guid-bb4e9e6a-7fff-133f-4e44-cb1d30def757"></span><p dir="ltr" style="line-height: 1.2; margin-top: 12pt; margin-bottom: 12pt;"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">Note : Each day he has to rent a bike independently and initially the fuel tank will be empty. Rental hours and fuel amount will be integer.</span></p>
</div>

## Input
 

<h4 class="railway-font">Input</h4>
<span id="docs-internal-guid-00c34927-7fff-ce7e-0881-37fefa6bd53b"></span><p dir="ltr" style="line-height: 1.295; margin-top: 0pt; margin-bottom: 0pt;"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">The first line contains one integer </span><strong><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">T (1 ≤ T ≤ </span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">2*10</span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><span style="vertical-align: super;">5</span></span></strong><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><strong>)</strong> </span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">— the number of test cases.</span></p><p><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">Each&nbsp; line contains two integers </span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><strong>N</strong></span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><strong> </strong>and </span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><strong>W </strong></span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">where </span><strong><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">(1 ≤ N ≤ 2*10</span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><span style="vertical-align: super;">5</span></span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"> , 1 ≤&nbsp;W ≤&nbsp;10</span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><span style="vertical-align: super;">18</span></span><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">)</span></strong><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;"><strong> </strong>— the number of days he will stay in Cox’s bazar and the amount of money.</span></p>

## Output
 
<p><span id="docs-internal-guid-c8cdfcd7-7fff-fa7e-88d4-027371f190cb"><span style="font-variant-numeric: normal; font-variant-east-asian: normal; vertical-align: baseline;">Output one number — <strong>maximum of minimum</strong> amount kilometers he can ride <strong>each day</strong>.</span></span></p>

## Samples

### Input

```
2
3 1500
4 990
```

### Output

```
100
0

```
## My Approach
```c++

```
