# Office problem

You are the owner of a coworking space like WeWork and your office building is rectangular. Your team just built wall partitions to create mini offices for startups. <br>
This office campus is represented by a 2D array of 1s (floor spaces) and 0s (walls). Each point on this array is a one foot by one foot square. You need to calculate the number of offices. <br>
A single office is bordered by walls and is constructed by placing floors next to each other, horizontally and/or vertically. Two 1s adjacent to each other horizontally or vertically are always part of the same office. <br>
<b>Function numOffices() has one parameter:</b> <br> 
grid - a 2D grid/array of 1s and 0s <br>
<b>In this problem, our input format is as follows:</b> <br>
The first line is the number of rows in the 2D array. The second line is the number of columns in the 2D array. The rest of the input contains the data to be processed.

## Here is an example of the raw input:

4 <br>
5 <br>
11110 <br>
11010 <br>
11000 <br>
00000<br>
<b>Expected:</b> Output returns the number of valid offices in the grid.

## Constraints

Assume all four edges of the grid are all surrounded by walls. 
Assume that the bounds of the array are the following: 
The total amount of elements in the array: width x height <= 10^6

## Example numOffices() 
#### Input:
4 <br>
5 <br>
11110 <br>
00000 <br>
00100 <br>
00011 <br>

#### Output:
3

## Solution

There's 3 offices in this grid, one made of four 1s on the top left, 
one made of one 1 in the middle, and one made of two 1s in the bottom right. <br>
Write a function numOffices() to solve this problem.