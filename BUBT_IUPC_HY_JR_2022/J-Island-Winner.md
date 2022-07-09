# [J. Island Winner](https://codeto.win/contest/43/problem/J)

<div id="statement">
<h3></h3><p></p><p align="justify" class="MsoNormal" style="margin-top:12.0000pt;margin-bottom:12.0000pt;text-align:justify;
text-justify:inter-ideograph;">CP land is a country with many islands. The islands are <strong>divided by water</strong>. In a few days there is going to be an election for the King of the island. D-joker and Jahin are two candidates who will fight for the throne. Since the islands are divided by water, there will be elections in all the islands separately. But the problem is to get the final result from all the islands.</p><p align="justify" class="MsoNormal" style="margin-top:12.0000pt;margin-bottom:12.0000pt;text-align:justify;
text-justify:inter-ideograph;">Luckily they have you to write a program that immediately announce the results.</p><p align="justify" class="MsoNormal" style="margin-top:12.0000pt;margin-bottom:12.0000pt;text-align:justify;
text-justify:inter-ideograph;">You are given the map of CP land as a 2D grid of <strong>N </strong>x <strong>M</strong> size . Consisting of following characters:</p><ul><li>‘D’ meaning this part of island has a vote for D-joker</li><li>‘J’ meaning this part of island has a vote for Jahin</li><li>‘#’ indicating water</li><li>‘=’  meaning it is part of the island but contains no vote.</li></ul><p align="justify" class="MsoNormal" style="margin-top:12.0000pt;margin-bottom:12.0000pt;text-align:justify;
text-justify:inter-ideograph;">Two cells of the grid is part of the same island if none of them is water and they have a common edge. Each cell has four edges.</p><p align="justify" class="MsoNormal" style="margin-top:12.0000pt;margin-bottom:12.0000pt;text-align:justify;
text-justify:inter-ideograph;">A candidate wins over a island if he has more vote than the other candidate in that island. A king is that one candidate who has won more islands than the other one.</p><p align="justify" class="MsoNormal" style="margin-top:12.0000pt;margin-bottom:12.0000pt;text-align:justify;
text-justify:inter-ideograph;">If both of them have same votes on an islands, no one conquers it, its a draw. If both win over same number of islands, None of them are King, ‘<strong>Jonogon</strong>’ is.</p>
</div>

## Input
 
<p>The first line gives an integer <strong>T (1 ≤ T ≤ 500)</strong>, denoting the number of test cases.</p>

## Output
 
<p>Announce the name of the king, “<strong>Jahin</strong>”, “<strong>D</strong><strong>-</strong><strong>joker</strong>” or “<strong>Jonogon</strong>”, without the quotes.</p>

## Samples

### Input

```
2

3 3
D=J
=J#
##D

5 5
#D###
##D##
##=##
#J###
#J###
```

### Output

```
Jonogon
D-joker

```
## My Approach
```c++

```
